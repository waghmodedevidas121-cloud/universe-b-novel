import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
studio_path = os.path.join(script_dir, "..", "New", "universe_b_writer_studio.html")
with open(studio_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Document Title
html = re.sub(
    r'<title>.*?</title>',
    r'<title>UNIVERSE B — Master Writer & Reader Studio</title>',
    html
)

# 2. Update Tailwind config colors (Warm Minimalist Dark Theme)
old_colors = """colors: {
                        studio: {
                            950: '#090a0f',
                            900: '#10121a',
                            850: '#161924',
                            800: '#1e2230',
                            700: '#2d3348',
                            accent: '#6366f1',
                            gold: '#f59e0b'
                        }
                    }"""

new_colors = """colors: {
                        studio: {
                            950: '#0c0d10',
                            900: '#131418',
                            850: '#181a20',
                            800: '#22242c',
                            700: '#2e313b',
                            accent: '#c99a5e',
                            gold: '#d97706'
                        }
                    }"""

html = html.replace(old_colors, new_colors)

# 3. Update Custom Styles in <style>
old_style_block = """/* Custom Scrollbars */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(16, 18, 26, 0.6);
        }
        ::-webkit-scrollbar-thumb {
            background: #2d3348;
            border-radius: 9999px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #4f46e5;
        }

        /* Rich Text Editor Custom Styling */
        #editor-content {
            outline: none;
            min-height: 65vh;
            line-height: 1.85;
            font-size: 1.125rem;
        }
        #editor-content p {
            margin-bottom: 1.25em;
        }
        #editor-content blockquote {
            border-left: 3px solid #6366f1;
            padding: 0.75rem 1.25rem;
            margin: 1.5rem 0;
            background: rgba(99, 102, 241, 0.08);
            border-radius: 0 0.5rem 0.5rem 0;
            font-style: italic;
        }"""

new_style_block = """/* Custom Scrollbars - Warm Minimalist Dark */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0c0d10;
        }
        ::-webkit-scrollbar-thumb {
            background: #272a33;
            border-radius: 9999px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #3c404d;
        }

        /* Rich Text Editor Custom Styling - Warm Editorial Reading */
        #editor-content {
            outline: none;
            min-height: 70vh;
            line-height: 1.95;
            font-size: 1.16rem;
            color: #ede9e3;
            font-family: 'Merriweather', 'Lora', Georgia, serif;
            letter-spacing: 0.01em;
        }
        #editor-content p {
            margin-bottom: 1.35em;
        }
        #editor-content blockquote {
            border-left: 3px solid #c99a5e;
            padding: 0.85rem 1.35rem;
            margin: 1.75rem 0;
            background: rgba(201, 154, 94, 0.06);
            border-radius: 0 0.35rem 0.35rem 0;
            font-style: italic;
            color: #d6cfc7;
        }"""

html = html.replace(old_style_block, new_style_block)

# 4. Clean up neon indigo in Tailwind classes
html = html.replace('bg-indigo-600 hover:bg-indigo-500 text-white', 'bg-[#c99a5e] hover:bg-[#b88648] text-[#0e0f12] font-semibold')
html = html.replace('text-indigo-400', 'text-[#d4a373]')
html = html.replace('text-indigo-300', 'text-[#e2bc91]')
html = html.replace('text-indigo-500', 'text-[#c99a5e]')
html = html.replace('border-indigo-500/40', 'border-[#c99a5e]/40')
html = html.replace('border-indigo-500/30', 'border-[#c99a5e]/30')
html = html.replace('border-indigo-500', 'border-[#c99a5e]')
html = html.replace('bg-indigo-600/15', 'bg-[#22201b]')
html = html.replace('bg-indigo-500/20', 'bg-[#c99a5e]/15')
html = html.replace('bg-indigo-500/10', 'bg-[#c99a5e]/10')
html = html.replace('selection:bg-indigo-500/30', 'selection:bg-[#c99a5e]/25')
html = html.replace('focus:border-indigo-500', 'focus:border-[#c99a5e]')
html = html.replace('focus:ring-indigo-500', 'focus:ring-[#c99a5e]')

# 5. Inject the Language Switcher inside Sidebar (Above Chapter List)
lang_switcher_html = """
                <!-- LANGUAGE SWITCHER BAR (NO DUPLICATES) -->
                <div class="px-3 pb-2.5 pt-1 shrink-0">
                    <div class="flex items-center justify-between text-[11px] text-stone-400 font-medium mb-1.5 px-0.5">
                        <span class="uppercase tracking-wider">Edition Track</span>
                        <span id="current-lang-indicator" class="text-[#c99a5e] font-semibold">Hindi Dub (Master)</span>
                    </div>
                    <div class="grid grid-cols-2 p-1 bg-[#0c0d10] border border-[#23252c] rounded-xl text-xs font-medium">
                        <button id="lang-btn-hi" onclick="switchLanguage('hi')" class="flex items-center justify-center gap-1.5 py-1.5 rounded-lg transition-all bg-[#23201b] border border-[#c99a5e]/50 text-[#f5eee6] shadow-sm">
                            <span>🇮🇳 Hindi Dub</span>
                        </button>
                        <button id="lang-btn-en" onclick="switchLanguage('en')" class="flex items-center justify-center gap-1.5 py-1.5 rounded-lg transition-all text-stone-400 hover:text-stone-200">
                            <span>🌐 English</span>
                        </button>
                    </div>
                </div>
"""

sidebar_target = '<div id="sidebar-tab-chapters" class="flex-1 flex flex-col overflow-hidden">'
if sidebar_target in html and 'id="lang-btn-hi"' not in html:
    html = html.replace(sidebar_target, sidebar_target + lang_switcher_html)

# 6. Inject Language Toggle into Top Header Bar
header_toggle_html = """
            <!-- Quick Language Switcher Header Button -->
            <button onclick="toggleLanguage()" class="flex items-center gap-2 text-xs font-medium bg-[#1a1b20] hover:bg-[#23252b] border border-[#2a2c35] text-stone-200 px-3 py-1.5 rounded-xl transition shadow-sm ml-2" title="Switch Language Track">
                <span id="header-lang-flag">🇮🇳</span>
                <span id="header-lang-label" class="text-[#d4a373] font-medium">Hindi Dub</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-stone-400"><path d="m7 15 5 5 5-5"/><path d="m7 9 5-5 5 5"/></svg>
            </button>
"""

header_target = '<div class="flex items-center gap-3">'
if header_target in html and 'header-lang-label' not in html:
    html = html.replace(header_target, header_target + header_toggle_html, 1)

# 7. Add Language State & Persistence Functions
script_funcs = """
        // --- Language Track Management ---
        let currentLang = localStorage.getItem('ub_preferred_lang') || 'hi';

        function updateLanguageUI() {
            const btnHi = document.getElementById('lang-btn-hi');
            const btnEn = document.getElementById('lang-btn-en');
            const indicator = document.getElementById('current-lang-indicator');
            const headerFlag = document.getElementById('header-lang-flag');
            const headerLabel = document.getElementById('header-lang-label');

            if (currentLang === 'hi') {
                if (btnHi) btnHi.className = "flex items-center justify-center gap-1.5 py-1.5 rounded-lg transition-all bg-[#23201b] border border-[#c99a5e]/50 text-[#f5eee6] shadow-sm";
                if (btnEn) btnEn.className = "flex items-center justify-center gap-1.5 py-1.5 rounded-lg transition-all text-stone-400 hover:text-stone-200";
                if (indicator) indicator.textContent = "Hindi Dub (Master)";
                if (headerFlag) headerFlag.textContent = "🇮🇳";
                if (headerLabel) headerLabel.textContent = "Hindi Dub";
            } else {
                if (btnEn) btnEn.className = "flex items-center justify-center gap-1.5 py-1.5 rounded-lg transition-all bg-[#23201b] border border-[#c99a5e]/50 text-[#f5eee6] shadow-sm";
                if (btnHi) btnHi.className = "flex items-center justify-center gap-1.5 py-1.5 rounded-lg transition-all text-stone-400 hover:text-stone-200";
                if (indicator) indicator.textContent = "English (Derived)";
                if (headerFlag) headerFlag.textContent = "🌐";
                if (headerLabel) headerLabel.textContent = "English";
            }
        }

        function switchLanguage(lang) {
            currentLang = lang;
            localStorage.setItem('ub_preferred_lang', lang);
            
            // Seamlessly swap current active chapter to counterpart in new language
            if (novelData && novelData.chapters) {
                const curId = novelData.activeChapterId;
                let targetId = curId;
                if (lang === 'hi' && curId.endsWith('-en')) {
                    targetId = curId.replace('-en', '-hi');
                } else if (lang === 'en' && curId.endsWith('-hi')) {
                    targetId = curId.replace('-hi', '-en');
                }
                
                const exists = novelData.chapters.some(c => c.id === targetId);
                if (exists) {
                    selectChapter(targetId, true);
                } else {
                    const firstOfLang = novelData.chapters.find(c => c.id.endsWith('-' + lang));
                    if (firstOfLang) selectChapter(firstOfLang.id, true);
                }
            }
            updateLanguageUI();
            renderChapterList();
        }

        function toggleLanguage() {
            switchLanguage(currentLang === 'hi' ? 'en' : 'hi');
        }

        // --- Reading State Persistence ---
        const UB_ACTIVE_CHAP_KEY = 'universe_b_active_chapter_v6';
        const UB_SCROLL_PREFIX   = 'universe_b_scroll_v6_';

        function saveCurrentReadingPosition() {
            try {
                if (!novelData || !novelData.activeChapterId) return;
                localStorage.setItem(UB_ACTIVE_CHAP_KEY, novelData.activeChapterId);
                const scrollEl = document.getElementById('editor-scroll-container');
                if (scrollEl) {
                    localStorage.setItem(UB_SCROLL_PREFIX + novelData.activeChapterId, scrollEl.scrollTop.toString());
                }
            } catch (e) {}
        }

        function restoreReadingPosition() {
            try {
                if (!novelData || !novelData.activeChapterId) return;
                const scrollEl = document.getElementById('editor-scroll-container');
                if (!scrollEl) return;
                const saved = localStorage.getItem(UB_SCROLL_PREFIX + novelData.activeChapterId);
                if (saved !== null) {
                    const top = parseInt(saved, 10);
                    if (!isNaN(top) && top > 0) {
                        setTimeout(() => { scrollEl.scrollTop = top; }, 80);
                        setTimeout(() => { scrollEl.scrollTop = top; }, 250);
                    }
                }
            } catch (e) {}
        }
"""

if 'function switchLanguage' not in html:
    html = html.replace("// --- Initialization ---", script_funcs + "\n        // --- Initialization ---")

# 8. Replace renderChapterList with clean filtered track (NO DUPLICATES)
new_render_chapters = """function renderChapterList() {
            const container = document.getElementById('chapter-list-container');
            // Filter to only display chapters of the active language track (NO DUPLICATES)
            const filteredChapters = novelData.chapters.filter(c => c.id.endsWith('-' + currentLang));
            
            document.getElementById('chapter-count-badge').textContent = filteredChapters.length;
            container.innerHTML = '';

            filteredChapters.forEach((chap, idx) => {
                const isActive = chap.id === novelData.activeChapterId;
                const wordCount = countWordsFromHTML(chap.content);
                
                let statusBadge = '';
                if (chap.status === 'Published') {
                    statusBadge = `<span class="w-2 h-2 rounded-full bg-emerald-400" title="Completed"></span>`;
                } else if (chap.status === 'Edited') {
                    statusBadge = `<span class="w-2 h-2 rounded-full bg-amber-400" title="Polished"></span>`;
                } else {
                    statusBadge = `<span class="w-2 h-2 rounded-full bg-stone-500" title="Draft"></span>`;
                }

                const item = document.createElement('div');
                item.className = `group flex items-center justify-between p-2.5 rounded-xl cursor-pointer border transition-all ${
                    isActive 
                        ? 'bg-[#22201b] border-[#c99a5e]/50 text-[#f5eee6] font-medium shadow-sm' 
                        : 'bg-transparent border-transparent hover:bg-studio-850 text-stone-300'
                }`;
                item.onclick = () => selectChapter(chap.id);

                const chapterNumberLabel = idx === 0 ? 'PROLOGUE' : `CH. ${idx}`;

                item.innerHTML = `
                    <div class="flex items-center gap-2.5 overflow-hidden">
                        <span class="w-1.5 h-6 rounded-full ${isActive ? 'bg-[#c99a5e]' : 'bg-transparent group-hover:bg-stone-700'} shrink-0 transition-colors"></span>
                        ${statusBadge}
                        <div class="overflow-hidden">
                            <div class="text-xs font-semibold truncate ${isActive ? 'text-white' : 'text-stone-200'}">${chapterNumberLabel}: ${escapeHTML(chap.title || 'Untitled')}</div>
                            <div class="text-[10px] text-stone-500 flex items-center gap-2 mt-0.5">
                                <span>${wordCount.toLocaleString()} words</span>
                                <span>•</span>
                                <span>${chap.status || 'Edited'}</span>
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                        ${filteredChapters.length > 1 ? `
                        <button onclick="deleteChapter(event, '${chap.id}')" class="p-1 rounded hover:bg-rose-500/20 text-slate-400 hover:text-rose-400" title="Delete Chapter">
                            <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
                        </button>` : ''}
                    </div>
                `;
                container.appendChild(item);
            });
            lucide.createIcons();
        }"""

idx_start = html.find('function renderChapterList()')
if idx_start != -1:
    idx_end = html.find('// --- Chapter Actions ---', idx_start)
    if idx_end != -1:
        html = html[:idx_start] + new_render_chapters + "\n\n        " + html[idx_end:]

# 9. Replace window.onload
new_onload = """window.onload = function () {
            loadFromStorage();

            // Restore preferred language
            const savedLang = localStorage.getItem('ub_preferred_lang');
            if (savedLang === 'hi' || savedLang === 'en') {
                currentLang = savedLang;
            }

            // Restore last-read chapter on refresh
            const lastRead = localStorage.getItem(UB_ACTIVE_CHAP_KEY);
            if (lastRead && novelData.chapters && novelData.chapters.some(c => c.id === lastRead)) {
                novelData.activeChapterId = lastRead;
                if (lastRead.endsWith('-hi')) currentLang = 'hi';
                else if (lastRead.endsWith('-en')) currentLang = 'en';
            } else {
                if (!novelData.activeChapterId.endsWith('-' + currentLang)) {
                    const firstOfLang = novelData.chapters.find(c => c.id.endsWith('-' + currentLang));
                    if (firstOfLang) novelData.activeChapterId = firstOfLang.id;
                }
            }

            updateLanguageUI();
            renderNovelHeader();
            renderChapterList();
            renderCodexList();
            loadChapterIntoEditor(novelData.activeChapterId);
            updateTotalNovelWords();
            lucide.createIcons();

            // Restore scroll position
            restoreReadingPosition();

            // Real-time scroll position persistence (debounced)
            const scrollEl = document.getElementById('editor-scroll-container');
            if (scrollEl) {
                let scrollTimer = null;
                scrollEl.addEventListener('scroll', () => {
                    clearTimeout(scrollTimer);
                    scrollTimer = setTimeout(saveCurrentReadingPosition, 100);
                }, { passive: true });
            }

            // Save on beforeunload
            window.addEventListener('beforeunload', saveCurrentReadingPosition);

            // Escape key exits Zen mode
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && document.body.classList.contains('zen-active')) {
                    toggleZenMode();
                }
            });
        };"""

idx_on_start = html.find('window.onload = function () {')
if idx_on_start != -1:
    idx_on_end = html.find('// --- LocalStorage Management ---', idx_on_start)
    if idx_on_end != -1:
        html = html[:idx_on_start] + new_onload + "\n\n        " + html[idx_on_end:]

# 10. Replace selectChapter
new_select = """function selectChapter(id, keepScroll = false) {
            if (!keepScroll) saveCurrentReadingPosition();
            novelData.activeChapterId = id;
            localStorage.setItem(UB_ACTIVE_CHAP_KEY, id);
            
            if (id.endsWith('-hi')) currentLang = 'hi';
            else if (id.endsWith('-en')) currentLang = 'en';
            updateLanguageUI();

            loadChapterIntoEditor(id);
            renderChapterList();
            saveToStorage();
            
            if (!keepScroll) {
                restoreReadingPosition();
            }
            if (!document.getElementById('reader-view').classList.contains('hidden')) {
                renderReaderPreview();
            }
            if (window.innerWidth < 1024) {
                document.getElementById('sidebar').classList.add('-translate-x-full');
            }
        }"""

idx_sel_start = html.find('function selectChapter(')
if idx_sel_start != -1:
    idx_sel_end = html.find('function loadChapterIntoEditor(', idx_sel_start)
    if idx_sel_end != -1:
        html = html[:idx_sel_start] + new_select + "\n\n        " + html[idx_sel_end:]

with open(studio_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("STUDIO_LANG_SWITCHER_SUCCESS")
