import server
import subprocess
from Tablo_Tk import *
from datetime import date
import json

'''
func ReadLog(filepath string) []string {
	fileHandle, err := os.Open(filepath)

	if err != nil {
		log.Fatal("Cannot open file")
	}
	defer fileHandle.Close()

	line := ""
	var cursor int64
	stat, _ := fileHandle.Stat()
	filesize := stat.Size()
	lines := [6]string{}
	lastCall := [5]bool{false, false, false, false, false}

	for {
		cursor -= 1
		fileHandle.Seek(cursor, io.SeekEnd)

		char := make([]byte, 1)
		fileHandle.Read(char)

		line = fmt.Sprintf("%s%s", string(char), line) // there is more efficient way
		if cursor == -filesize {
			break
		}
	}

	allLine := strings.Split(line, "\n")
	for _, e := range allLine {
		if strings.Contains(e, ";01;") && !lastCall[0] {
			lines[0] = e
		} else if strings.Contains(e, ";02;") && !lastCall[1] {
			lines[1] = e
		} else if strings.Contains(e, ";03;") && !lastCall[2] {
			lines[2] = e
		} else if strings.Contains(e, ";04;") && !lastCall[3] {
			lines[3] = e
		} else if strings.Contains(e, ";05;") && !lastCall[4] {
			lines[4] = e
		}
		if lastCall[0] || lastCall[1] || lastCall[2] || lastCall[3] || lastCall[4] {
			break
		}
	}

	return lines[:]'''
 
def readLog(filepath, NumTubs, Prs, Ids):
    with open(filepath, encoding='utf-8') as f:
        fileHandle = f.readlines()
        fileHandle.reverse()
    today = date.today()
    today = str(today).replace('-', '/')
    lastCall = [False, False, False, False, False]
    for e in fileHandle:
        data = e.split(';')
        logDate = data[0].split()[0]
        if logDate != today:
            continue
        else:
            if data[1] == '01' and not(lastCall[0]):
                Id = Ids[0]
                Id.set(data[1])
                NumTub = NumTubs[0]
                if data[2] == '----':
                    NumTub.set('')
                else:
                    NumTub.set(data[2])
                Pr = Prs[0]
                Pr.set(data[3])
                lastCall[0] = True
            elif data[1] == '02' and not(lastCall[1]):
                Id = Ids[1]
                Id.set(data[1])
                NumTub = NumTubs[1]
                if data[2] == '----':
                    NumTub.set('')
                else:
                    NumTub.set(data[2])
                Pr = Prs[1]
                Pr.set(data[3])
                lastCall[1] = True
            elif data[1] == '03' and not(lastCall[2]):
                Id = Ids[2]
                Id.set(data[1])
                NumTub = NumTubs[2]
                if data[2] == '----':
                    NumTub.set('')
                else:
                    NumTub.set(data[2])
                Pr = Prs[2]
                Pr.set(data[3])
                lastCall[2] = True
            elif data[1] == '04' and not(lastCall[3]):
                Id = Ids[3]
                Id.set(data[1])
                NumTub = NumTubs[3]
                if data[2] == '----':
                    NumTub.set('')
                else:
                    NumTub.set(data[2])
                Pr = Prs[3]
                Pr.set(data[3])
                lastCall[3] = True
            elif data[1] == '05' and not(lastCall[4]):
                Id = Ids[4]
                Id.set(data[1])
                NumTub = NumTubs[4]
                if data[2] == '----':
                    NumTub.set('')
                else:
                    NumTub.set(data[2])
                Pr = Prs[4]
                Pr.set(data[3])
                lastCall[4] = True
        if lastCall[0] and lastCall[1] and lastCall[2] and lastCall[3] and lastCall[4]:
            break
    return (NumTubs, Prs, Ids)

with open('conf.json', 'r') as f:
    conf = json.load(f)

host = conf['server']['address']
port = conf['server']['port']
server_name = conf['server']['server_name']
serv = server.MyHTTPServer(host, port, server_name)
check = 1

#Создание клиента

root, NumTubs, Prs, Ids = createTablo()
#Создание и вывод QR-кодов
QRimage = PhotoImage(file="static\QR.png") #QR.png resolution=960x506
QRcodes = ttk.Label(root, image=QRimage)
QRcodes.grid(row=1, column=1, sticky=SE)
if check:
    NumTubs, Prs, Ids = readLog("logs.log", NumTubs, Prs, Ids)
    check = 0
    
#Создание GET запроса

root.mainloop()


