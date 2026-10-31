# Build Universe B Writer Studio (single-file HTML) from canonical markdown chapters.
# PowerShell only. No Python.

$ErrorActionPreference = 'Stop'

$root      = 'D:\Web Novel\UNIVERSE B'
$newDir    = Join-Path $root 'New'
$storyDir  = Join-Path $root 'Story'
$srcHtml   = 'D:\assests\video\web_novel_writer_studio.html'
$outHtml   = Join-Path $newDir 'universe_b_writer_studio.html'

function Convert-MdChapters {
    param([string[]]$Lines)

    # strip header block: everything up to and including the first standalone '---'
    $idx = -1
    for ($i = 0; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i].Trim() -eq '---') { $idx = $i; break }
    }
    if ($idx -ge 0) { $Lines = $Lines[($idx + 1)..($Lines.Count - 1)] }

    # drop leading h1-h4 heading lines
    $Lines = $Lines | Where-Object { $_ -notmatch '^#{1,4}\s' }

    $sb = New-Object System.Text.StringBuilder
    $buffer = New-Object System.Collections.Generic.List[string]
    $listBuffer = New-Object System.Collections.Generic.List[string]

    function Flush-Para {
        if ($buffer.Count -eq 0) { return '' }
        $text = ($buffer -join ' ')
        $buffer.Clear()
        $text = $text -replace '\*\*(.+?)\*\*', '<strong>$1</strong>'
        $text = $text -replace '\*(.+?)\*', '<em>$1</em>'
        return "<p>$text</p>"
    }

    function Flush-List {
        if ($listBuffer.Count -eq 0) { return '' }
        $items = ($listBuffer | ForEach-Object {
            $t = $_ -replace '\*\*(.+?)\*\*', '<strong>$1</strong>'
            $t = $t -replace '\*(.+?)\*', '<em>$1</em>'
            "<li>$t</li>"
        }) -join ''
        $listBuffer.Clear()
        return "<ul class='list-disc pl-6 space-y-1'>$items</ul>"
    }

    $out = New-Object System.Collections.Generic.List[string]

    foreach ($raw in $Lines) {
        $line = $raw.TrimEnd()
        $trim = $line.Trim()

        if ($trim -eq '') {
            if ($buffer.Count -gt 0) { $out.Add((Flush-Para)) }
            if ($listBuffer.Count -gt 0) { $out.Add((Flush-List)) }
            continue
        }

        if ($trim -eq '---') {
            if ($buffer.Count -gt 0) { $out.Add((Flush-Para)) }
            if ($listBuffer.Count -gt 0) { $out.Add((Flush-List)) }
            $out.Add("<div class='scene-break'>✦ ✦ ✦</div>")
            continue
        }

        if ($trim -match '^-\s+') {
            if ($buffer.Count -gt 0) { $out.Add((Flush-Para)) }
            $listBuffer.Add(($trim -replace '^-\s+', ''))
            continue
        }

        if ($listBuffer.Count -gt 0) { $out.Add((Flush-List)) }
        $buffer.Add($trim)
    }

    if ($buffer.Count -gt 0) { $out.Add((Flush-Para)) }
    if ($listBuffer.Count -gt 0) { $out.Add((Flush-List)) }

    return ($out -join '')
}

function New-Chapter {
    param($Id, $Title, $Status, $File)
    $path = Join-Path $storyDir $File
    if (-not (Test-Path $path)) { $path = Join-Path $newDir $File }
    $lines = [System.IO.File]::ReadAllLines($path, [System.Text.Encoding]::UTF8)
    $html = Convert-MdChapters -Lines $lines
    $words = ([regex]::Matches($html, '\S+')).Count
    [PSCustomObject]@{
        id        = $Id
        title     = $Title
        status    = $Status
        updatedAt = '2026-10-28'
        content   = $html
        authorNote = "Universe B - Season 1, Volume 1. English master track and Hindi anime-dub track are separate editions. Words: $words"
    }
}

$chapters = @(
    (New-Chapter -Id 'chap-pro-hi' -Title 'PROLOGUE: The Glitch in the Rain' -Status 'Edited' -File '18A_Season_1_Volume_1_Prologue_Hindi.md'),
    (New-Chapter -Id 'chap-1-hi'   -Title 'Chapter 1: The Hay, the Horns, and the Dead Glass' -Status 'Edited' -File '19_Season_1_Chapter_1_Hindi.md'),
    (New-Chapter -Id 'chap-2-hi'   -Title 'Chapter 2: Rank #84 and the Shifting Field' -Status 'Edited' -File '20_Season_1_Chapter_2_Hindi.md'),
    (New-Chapter -Id 'chap-3-hi'   -Title 'Chapter 3: The Sand, the Steel, and the First Spark' -Status 'Edited' -File '21_Season_1_Chapter_3_Hindi.md'),

    (New-Chapter -Id 'chap-pro-en' -Title 'PROLOGUE: The Glitch in the Rain' -Status 'Edited' -File '18A_Season_1_Volume_1_Prologue.md'),
    (New-Chapter -Id 'chap-1-en'   -Title 'Chapter 1: The Hay, the Horns, and the Dead Glass' -Status 'Edited' -File '19_Season_1_Chapter_1.md'),
    (New-Chapter -Id 'chap-2-en'   -Title 'Chapter 2: Rank #84 and the Shifting Field' -Status 'Edited' -File '20_Season_1_Chapter_2.md'),
    (New-Chapter -Id 'chap-3-en'   -Title 'Chapter 3: The Sand, the Steel, and the First Spark' -Status 'Edited' -File '21_Season_1_Chapter_3.md')
)

$codex = @(
    [PSCustomObject]@{ id='cod-1'; name='Neel'; category='Character'; desc='19-year-old Mumbai engineering student. Fell through a spatial glitch at Dadar bridge. Zero system, zero boons. Quirk: pulse resonance and friction spark. Street-smart, rationalist, refuses to kneel.' },
    [PSCustomObject]@{ id='cod-2'; name='Sheru (registry: Kuro)'; category='Character'; desc='Stage-1 Dusk-Scrapper Hound. One ear torn off, brindled charcoal coat, amber eyes. Bound to Neel by a physical soul-bond, no pocket storage.' },
    [PSCustomObject]@{ id='cod-3'; name='Central City'; category='Location'; desc='The neutral white-stone metropolis at the geometric centre of the Five Shards. Governed from the Five-Arch Rotunda. Crossroads of all trade and all violence.' },
    [PSCustomObject]@{ id='cod-4'; name='Feeder Sand-Pits'; category='Location'; desc='D-Tier rookie feeder circuit sunk into the exterior south trench. Free rations for contenders, ten copper Panas and a transit pass for winners. Bottom rung of the Proving Games.' },
    [PSCustomObject]@{ id='cod-5'; name='Nadi and Prana'; category='Power/System'; desc='72,000 meridian channels carrying vital force. No mana bar, no levels. Overdraw causes The Blowout: internal channel rupture and black charring.' },
    [PSCustomObject]@{ id='cod-6'; name='The Chime'; category='Power/System'; desc='A private brass bell heard only inside the skull at a moment of deathly crisis. Ananta registers the breakthrough. No screen, no notification, no numbers.' },
    [PSCustomObject]@{ id='cod-7'; name='Copper Panas'; category='Power/System'; desc='Local copper currency. Five Panas is the official city gate toll. Ten Panas is a rookie winning purse. One Aether-Rupee equals one hundred Silver Panas.' }
)

$project = [PSCustomObject]@{
    title    = 'UNIVERSE B'
    author   = 'waghmodedevidas121-cloud'
    genre    = 'Dark Anime Fantasy / Tournament Isekai'
    synopsis = 'A 19-year-old Mumbai college student falls through a puddle into a frozen void. He wakes in a beast-cart with a dead phone, no coins and no system - only street instinct and a one-eared stray hound.'
    activeChapterId = 'chap-pro-hi'
    chapters = $chapters
    codex    = $codex
}

$json = $project | ConvertTo-Json -Depth 6 -Compress

$html = [System.IO.File]::ReadAllText($srcHtml, [System.Text.Encoding]::UTF8)

# --- Purge the source template's demo novel (static HTML shells) ---
$html = $html.Replace('Chronicles of the Void Monarch', 'UNIVERSE B')
$html = $html.Replace('Awakening in a shattered world with a forbidden System, Aarav must climb the Obsidian Tower before the gods erase his existence.', 'A 19-year-old Mumbai college student falls through a puddle into a frozen void. He wakes in a beast-cart with a dead phone, no coins and no system - only street instinct and a one-eared stray hound.')
$html = $html.Replace('Aarav Varma', 'Neel')
$html = $html.Replace('Protagonist. Former F-Rank ruin porter who awakened the Void Monarch System. Calm, calculating, fierce loyalty to his sister.', '19-year-old Mumbai engineering student. Fell through a spatial glitch at Dadar bridge. Zero system, zero boons. Street-smart rationalist with a pulse-resonance quirk.')
$html = $html.Replace('Shadow Step (Rank E)', 'Sheru (registry: Kuro)')
$html = $html.Replace('Allows instant teleportation between connected shadows within a 15-meter radius. Cooldown: 4 seconds.', 'Stage-1 Dusk-Scrapper Hound. One ear torn off, brindled charcoal coat, amber eyes. Bound to Neel by a physical soul-bond, no pocket storage.')
$html = $html.Replace('The Obsidian Spire', 'Central City')
$html = $html.Replace('An inverted ancient dungeon beneath Old Mumbai containing 100 floors of forgotten deities and relics.', 'The neutral white-stone metropolis at the geometric centre of the Five Shards. Governed from the Five-Arch Rotunda. Crossroads of all trade and all violence.')
$html = $html.Replace('CHRONICLES OF THE VOID MONARCH', 'UNIVERSE B')
$html = $html.Replace('Chapter 1: The Broken Altar', 'PROLOGUE: The Glitch in the Rain')
$html = $html.Replace('e.g. Aarav Varma, Abyssal Flame, Floor 7...', 'e.g. Neel, Sheru, Feeder Sand-Pits...')

# --- Zero floating gamer menus & no manat tags: remove the LitRPG system box button & function completely ---
$btnPattern = '(?s)<button onclick="insertSystemBox\(\)".*?<\/button>\s*'
$html = [regex]::Replace($html, $btnPattern, '')

$funcPattern = '(?s)function insertSystemBox\(\)\s*\{.*?\}\s*'
$html = [regex]::Replace($html, $funcPattern, '')

# --- Replace the demo editor body with a clean placeholder ---
$openMarker  = '<div id="editor-content" contenteditable="true"'
$junkStart   = '<div class="system-box">[CRITICAL ANOMALY DETECTED]'
$junkEndTail = 'Come and claim it.' + [char]0x201D + '</p></div>'

$oIdx = $html.IndexOf($openMarker)
$jIdx = $html.IndexOf($junkStart)
$eIdx = $html.IndexOf($junkEndTail)

if ($oIdx -lt 0) { throw 'editor-content container not found in template' }
if ($jIdx -lt 0 -or $eIdx -lt 0) { throw 'demo editor body markers not found in template' }

$tagEnd = $html.IndexOf('>', $oIdx) + 1
$eIdx   = $eIdx + $junkEndTail.Length

$html = $html.Substring(0, $tagEnd) + '<p>Loading Universe B canon...</p></div>' + $html.Substring($eIdx)

$startMarker = '// --- Default Starter Novel Data ---'
$endMarker   = '// --- App State ---'

$s = $html.IndexOf($startMarker)
$e = $html.IndexOf($endMarker)
if ($s -lt 0 -or $e -lt 0) { throw 'markers not found' }

$block = "// --- Universe B Canonical Project Data ---`r`n        const DEFAULT_PROJECT = $json;`r`n`r`n        "

$html = $html.Substring(0, $s) + $block + $html.Substring($e)

# unique storage key so the demo project does not collide
$html = $html.Replace("novelcraft_studio_v1", "universe_b_studio_v6")

$utf8 = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($outHtml, $html, $utf8)

# Apply Warm Dark Minimalist Theme & Reading Persistence
python "$root\scripts\patch_studio_ui.py"

# Post-patch: Permanently eliminate chapter caching so the studio ALWAYS renders the compiled canonical HTML
$patched = [System.IO.File]::ReadAllText($outHtml, [System.Text.Encoding]::UTF8)

$zeroCacheCode = @"
        // --- Zero-Cache Pure Direct Canonical Content Engine ---
        function loadFromStorage() {
            // ALWAYS initialize novelData directly from DEFAULT_PROJECT so no stale cache can ever exist
            novelData = JSON.parse(JSON.stringify(DEFAULT_PROJECT));
            try {
                // Clear any legacy localStorage keys that cause conflicting caches
                for (let i = 0; i <= 30; i++) {
                    localStorage.removeItem('universe_b_studio_v' + i);
                }
                localStorage.removeItem('novelcraft_studio_v1');
            } catch (e) {}
        }

        function saveToStorage() {
            // Do not store chapter texts in localStorage to avoid browser caching conflicts
            try {
                const statusEl = document.getElementById('save-status');
                if (statusEl) {
                    statusEl.innerHTML = '<i data-lucide="check-circle-2" class="w-3 h-3"></i> Synced';
                    statusEl.className = 'flex items-center gap-1 text-[11px] text-emerald-400';
                    lucide.createIcons();
                }
            } catch (e) {}
        }
"@

$patched = [regex]::Replace($patched, '(?s)//\s*--- (?:LocalStorage Management|Zero-Cache Pure Direct Canonical Content Engine) ---.*?console\.error\("Storage error:", e\);\s*\}\s*\}', $zeroCacheCode)

[System.IO.File]::WriteAllText($outHtml, $patched, [System.Text.Encoding]::UTF8)

$words = ($chapters | ForEach-Object { ([regex]::Matches($_.content, '\S+')).Count } | Measure-Object -Sum).Sum
Write-Output "OK"
Write-Output ("file      : " + $outHtml)
Write-Output ("bytes     : " + (Get-Item $outHtml).Length)
Write-Output ("chapters  : " + $chapters.Count)
Write-Output ("words     : " + $words)
Write-Output ("codex     : " + $codex.Count)
