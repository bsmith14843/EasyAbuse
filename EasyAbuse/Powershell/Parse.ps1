$fileName = Read-Host "What is the file name?"
$fileWithExt = ".\" + $fileName + ".csv"

$ipReg = '^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'


$dingo = 1

if(Test-Path -Path $fileWithExt){
	$csv = Import-Csv -Path $fileWithExt
	$topObject = ($csv | Get-Member -MemberType NoteProperty).Name
		
	if($topObject -match $ipReg){
		Write-Output "The Top Position at $dingo has a valid IP"
		
	}
	
	foreach ($row in $csv){
		
		if($row.$topObject -match $ipReg){
			#Write-Output "$($row.$topObject) is at position $dingo"
			Write-Output "Position $dingo has a valid IP"
		}else{
			#Write-Output "$($row.$topObject) is at position $dingo"
			Write-Output "Position $dingo does NOT have a valid IP"
		}
		$dingo ++
	}
		
} else{
	Write-Output "File not found!"
}
