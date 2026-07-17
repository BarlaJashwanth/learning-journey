## Append mode : adds new data to the end of an existing file without deleting or overwriting the original content
fh = open("file.txt","at")
fh.write("\nThis content is written by using a mode\n")
fh.close()
## if you check file.txt you can see new txt is been added

## What if we use append mode for the file which is not existing
### it simply creates new file and add text like w mode , but w mode if we use on existing file it overwrites on it but in case of a mode on existing file it just add the new text at end
### but on non existing files if we use a or w mode both simply create and write text in it ...




