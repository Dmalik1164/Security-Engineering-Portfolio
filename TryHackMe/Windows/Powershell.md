# Windows PowerShell Notes — TryHackMe

## PowerShell Basics

PowerShell uses **objects** instead of plain text.  
Objects contain:

- **Properties** → characteristics/data
- **Methods** → actions/functions

Example:
A car object may contain:

- Properties: `Color`, `Model`, `FuelLevel`
- Methods: `Drive()`, `HonkHorn()`, `Refuel()`

---

## Cmdlets

PowerShell commands are called **cmdlets**.

They follow a:

Verb-Noun

naming structure.

Examples:

- `Get-Content` → retrieves file contents
- `Set-Location` → changes current directory

---

# Useful Commands

## Help & Discovery

```powershell
Get-Help
Get-Command
Get-Command -Name "..."
Get-Alias
Get-Help <command> -Examples

'''Navigation & File Management:

Get-ChildItem
Set-Location -Path ".\..."

New-Item -Path ".\...\"
Remove-Item -Path
Copy-Item -Path
Get-Content -Path

Piping

PowerShell uses | to pass output from one command to another.

Examples:

Get-ChildItem | Sort-Object

Get-ChildItem | Where-Object -Property "Extension" -eq "txt"

Get-ChildItem | Where-Object -Property "Name" -like "ship*"

Get-ChildItem | Select-Object Name, Length

Get-ChildItem |
Sort-Object Length -Descending |
Select-Object -First 1

Searching Text
Select-String -Path ".\captain-hat.txt" -Pattern "hat"

Used to search for specific text inside files.

Comparison Operators
-gt   # Greater than
-lt   # Less than
-eq   # Equal to
-like # Pattern matching












