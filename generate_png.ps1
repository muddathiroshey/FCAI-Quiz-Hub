Add-Type -AssemblyName System.Drawing

# Function to create course images
function New-CourseImage {
    param(
        [string]$outFile,
        [string]$code,
        [string]$title,
        [string]$desc,
        [array]$statVals,
        [string]$footer
    )
    
    $bmp = New-Object System.Drawing.Bitmap(1200, 1200)
    $graphics = [System.Drawing.Graphics]::FromImage($bmp)
    
    # Dark background
    $graphics.Clear([System.Drawing.Color]::FromArgb(15, 23, 42))
    
    # Fonts
    $titleFont = New-Object System.Drawing.Font("Arial", 90, [System.Drawing.FontStyle]::Bold)
    $subtitleFont = New-Object System.Drawing.Font("Arial", 55, [System.Drawing.FontStyle]::Bold)
    $labelFont = New-Object System.Drawing.Font("Arial", 22)
    $statFont = New-Object System.Drawing.Font("Arial", 48, [System.Drawing.FontStyle]::Bold)
    
    # Brushes
    $whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $accentBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(96, 165, 250))
    $grayBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(107, 114, 128))
    
    # Draw elements
    $graphics.DrawString("CAPITAL UNIVERSITY", $labelFont, $accentBrush, 80, 60)
    $graphics.DrawString($code, $titleFont, $whiteBrush, 80, 200)
    $graphics.DrawString($title, $subtitleFont, $whiteBrush, 80, 380)
    $graphics.DrawString($desc, $labelFont, $grayBrush, 80, 540)
    
    # Stats
    $statLabels = @("QUESTIONS", "CHAPTERS", "FORMAT")
    for ($i = 0; $i -lt $statVals.Count; $i++) {
        $xPos = 80 + ($i * 350)
        $graphics.DrawString([string]$statVals[$i], $statFont, $whiteBrush, $xPos, 700)
        $graphics.DrawString($statLabels[$i], $labelFont, $grayBrush, $xPos, 800)
    }
    
    if ($footer) {
        $graphics.DrawString($footer, $labelFont, $grayBrush, 80, 1050)
    }
    
    $bmp.Save($outFile)
    $graphics.Dispose()
    $bmp.Dispose()
    Write-Host "Created $(Split-Path -Leaf $outFile)"
}

# Generate images
New-CourseImage "og-images\it.png" "IT 223" "Internet Technology" "Chapters 1–6 · 203 Questions" @(203, 6, "MCQ") "Protocols · Networks · Addressing"
New-CourseImage "og-images\os.png" "CS 241" "Operating Systems" "Lectures 0–8 · 117 Questions" @(117, 9, "MC/TF") "Dr. Ahmed Hisham Mostafa"
New-CourseImage "og-images\accounting.png" "HU 323" "Fundamentals of Accounting" "Chapters 1–2 · 47 Questions" @(47, 2, "MCQ") "Dr. Hamdy Habl"
New-CourseImage "og-images\networks.png" "IT 222" "Computer Networks 1" "90 Questions · Subnetting" @(90, "MC/TF", "") "Dr. Islam Zakaria"

# Quiz Hub main
$bmp = New-Object System.Drawing.Bitmap(1200, 1200)
$graphics = [System.Drawing.Graphics]::FromImage($bmp)
$graphics.Clear([System.Drawing.Color]::FromArgb(15, 23, 42))

$titleFont = New-Object System.Drawing.Font("Arial", 100, [System.Drawing.FontStyle]::Bold)
$labelFont = New-Object System.Drawing.Font("Arial", 28)
$whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$accentBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(96, 165, 250))

$graphics.DrawString("CAPITAL UNIVERSITY", $labelFont, $accentBrush, 80, 150)
$graphics.DrawString("Course", $titleFont, $whiteBrush, 80, 350)
$graphics.DrawString("Quiz Hub", $titleFont, $whiteBrush, 80, 550)
$graphics.DrawString("Practice quizzes for your courses", $labelFont, $accentBrush, 80, 900)

$bmp.Save("og-images\quiz-hub.png")
$graphics.Dispose()
$bmp.Dispose()
Write-Host "Created quiz-hub.png"

Write-Host "All PNG images generated!"
