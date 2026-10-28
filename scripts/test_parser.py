import os
import re
import html

def md_to_html(md_text):
    lines = md_text.splitlines()
    html_lines = []
    in_code = False
    in_table = False
    in_ul = False
    in_ol = False
    code_lang = ""
    code_buf = []
    
    for line in lines:
        # Code blocks
        if line.strip().startswith("```"):
            if in_code:
                in_code = False
                escaped = html.escape("\n".join(code_buf))
                html_lines.append(f'<pre><code class="language-{code_lang}">{escaped}</code></pre>')
                code_buf = []
            else:
                in_code = True
                code_lang = line.strip()[3:].strip()
            continue
            
        if in_code:
            code_buf.append(line)
            continue
            
        # Tables
        if "|" in line and (line.strip().startswith("|") or line.strip().endswith("|")):
            if re.match(r'^\s*\|?\s*[-:]+[-| :]*\|\s*$', line):
                # separator line
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not in_table:
                in_table = True
                html_lines.append('<div class="table-container"><table><thead><tr>')
                for c in cells:
                    html_lines.append(f'<th>{inline_format(c)}</th>')
                html_lines.append('</tr></thead><tbody>')
            else:
                html_lines.append('<tr>')
                for c in cells:
                    html_lines.append(f'<td>{inline_format(c)}</td>')
                html_lines.append('</tr>')
            continue
        else:
            if in_table:
                in_table = False
                html_lines.append('</tbody></table></div>')
                
        # Lists
        ul_match = re.match(r'^\s*[-*+]\s+(.*)$', line)
        ol_match = re.match(r'^\s*(\d+)\.\s+(.*)$', line)
        
        if ul_match:
            if not in_ul:
                in_ul = True
                html_lines.append('<ul>')
            html_lines.append(f'<li>{inline_format(ul_match.group(1))}</li>')
            continue
        else:
            if in_ul:
                in_ul = False
                html_lines.append('</ul>')
                
        if ol_match:
            if not in_ol:
                in_ol = True
                html_lines.append('<ol>')
            html_lines.append(f'<li>{inline_format(ol_match.group(2))}</li>')
            continue
        else:
            if in_ol:
                in_ol = False
                html_lines.append('</ol>')
                
        # Empty lines
        stripped = line.strip()
        if not stripped:
            continue
            
        # Headers
        h_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if h_match:
            level = len(h_match.group(1))
            h_text = h_match.group(2)
            h_id = re.sub(r'[^a-zA-Z0-9_-]', '_', h_text.lower()).strip('_')
            html_lines.append(f'<h{level} id="{h_id}">{inline_format(h_text)}</h{level}>')
            continue
            
        # Horizontal rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            html_lines.append('<hr>')
            continue
            
        # Blockquote
        if stripped.startswith(">"):
            b_text = stripped.lstrip(">").strip()
            html_lines.append(f'<blockquote>{inline_format(b_text)}</blockquote>')
            continue
            
        # Paragraph
        html_lines.append(f'<p>{inline_format(stripped)}</p>')
        
    if in_code:
        escaped = html.escape("\n".join(code_buf))
        html_lines.append(f'<pre><code>{escaped}</code></pre>')
    if in_table:
        html_lines.append('</tbody></table></div>')
    if in_ul:
        html_lines.append('</ul>')
    if in_ol:
        html_lines.append('</ol>')
        
    return "\n".join(html_lines)

def inline_format(text):
    # Bold italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    # Tags
    text = re.sub(r'(#[\w-]+)', r'<span class="badge">\1</span>', text)
    return text

print("Parser defined successfully")
