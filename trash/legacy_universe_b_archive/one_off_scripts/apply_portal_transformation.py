import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
portal_template_path = os.path.join(current_dir, "portal_template.html")
story_content_path = os.path.join(current_dir, "story_html_content.py")

with open(story_content_path, "r", encoding="utf-8") as f:
    # Exec to get story_chronicle_html
    local_scope = {}
    exec(f.read(), {}, local_scope)
    story_chronicle_html = local_scope["story_chronicle_html"]

from update_portal_template import story_css

with open(portal_template_path, "r", encoding="utf-8") as f:
    template = f.read()

# 1. Insert CSS if not present
if "/* STORY CHRONICLE & IMMERSIVE NOVEL-GRADE PORTAL STYLES */" not in template:
    template = template.replace("</style>", story_css + "\n</style>")

# 2. Update sidebar navigation
old_sidebar_nav = """  <nav class="nav-menu" id="navMenu">
    <!-- Populated by JS -->
  </nav>"""

new_sidebar_nav = """  <div class="story-nav-section">
    <div class="nav-section-label">CHRONICLE MODES</div>
    <div class="nav-item active" id="btnStoryChronicle" onclick="showStoryChronicle()">
      <div class="nav-item-title">
        <span>📖</span>
        <span>Living Story Chronicle</span>
      </div>
      <span class="file-count" style="background: rgba(245, 158, 11, 0.25); color: var(--accent-gold-light); font-weight: bold;">EPIC</span>
    </div>
  </div>

  <div class="nav-section-label" style="padding: 10px 18px 4px; font-size: 0.68rem; font-family: var(--font-mono); color: var(--text-dim); letter-spacing: 1.5px; text-transform: uppercase;">
    CANONICAL DEEP ARCHIVE
  </div>
  <nav class="nav-menu" id="navMenu">
    <!-- Populated by JS -->
  </nav>"""

if old_sidebar_nav in template:
    template = template.replace(old_sidebar_nav, new_sidebar_nav)
elif 'id="btnStoryChronicle"' not in template:
    print("WARNING: Could not find exact old_sidebar_nav in template")

# 3. Update content-viewport to wrap docArchiveView and add storyChronicleView
old_viewport = """  <div class="content-viewport" id="contentViewport">
    <!-- Active Category View -->
    <div id="categoryHeader"></div>
    <div id="sopyaBox"></div>
    <div class="doc-tabs-bar" id="docTabsBar"></div>
    <div class="doc-article" id="docArticle"></div>
  </div>"""

new_viewport = f"""  <div class="content-viewport" id="contentViewport">
    <!-- 1. The Living Story Chronicle (Default View) -->
    <div id="storyChronicleView">
{story_chronicle_html}
    </div>

    <!-- 2. Master Canonical Document Archive -->
    <div id="docArchiveView" style="display: none;">
      <div style="margin-bottom: 18px;">
        <button class="story-mode-switch-btn" onclick="showStoryChronicle()">
          <span>📖</span> Return to The Living Story Chronicle
        </button>
      </div>
      <div id="categoryHeader"></div>
      <div id="sopyaBox"></div>
      <div class="doc-tabs-bar" id="docTabsBar"></div>
      <div class="doc-article" id="docArticle"></div>
    </div>
  </div>"""

if old_viewport in template:
    template = template.replace(old_viewport, new_viewport)
elif 'id="storyChronicleView"' not in template:
    print("WARNING: Could not find exact old_viewport in template")

# 4. Add JS functions for showStoryChronicle and updating init()
js_addition = """
function showStoryChronicle() {
  document.getElementById("storyChronicleView").style.display = "block";
  document.getElementById("docArchiveView").style.display = "none";
  
  document.getElementById("btnStoryChronicle").classList.add("active");
  document.querySelectorAll("#navMenu .nav-item").forEach(item => item.classList.remove("active"));
  
  document.getElementById("bcFolder").innerText = "Epic Chronicle";
  document.getElementById("bcFile").innerText = "The Story of Universe B";
  document.getElementById("contentViewport").scrollTop = 0;
}
"""

old_init = """function init() {
  renderSidebar();
  selectCategory(0, 0);
}"""

new_init = """function init() {
  renderSidebar();
  showStoryChronicle();
}"""

if js_addition.strip() not in template:
    template = template.replace("function selectCategory(catIdx, fileIdx) {", js_addition + "\nfunction selectCategory(catIdx, fileIdx) {\n  document.getElementById('storyChronicleView').style.display = 'none';\n  document.getElementById('docArchiveView').style.display = 'block';\n  const btnStory = document.getElementById('btnStoryChronicle');\n  if (btnStory) btnStory.classList.remove('active');\n")

if old_init in template:
    template = template.replace(old_init, new_init)

with open(portal_template_path, "w", encoding="utf-8") as f:
    f.write(template)

print("portal_template.html successfully transformed into an immersive Story Chronicle portal!")
