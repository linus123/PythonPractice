$pythonExec = "C:\Users\linus\AppData\Local\Programs\Python\Python37-32\python.exe"
$resultFile = "output.txt"

if (Test-Path $resultFile) {
    Remove-Item $resultFile
}

Get-Content .\10138.txt | &$pythonExec .\cdvii.py > $resultFile
