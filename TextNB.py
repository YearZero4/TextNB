### CONVERSOR DE NUMERO A TEXTO ###
def banner():
 print(f'''   _____         _   _   _ ____
  |_   _|____  _| |_| \\ | | __ )
    | |/ _ \\ \\/ / __|  \\| |  _ \\
    | |  __/>  <| |_| |\\  | |_) |
    |_|\\___/_/\\_\\\\__|_| \\_|____/

 Presione [ENTER] Para Continuar...
	''')

units=['', 'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
teens = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
dc=['', "veinti", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
ctn = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def convert(number):
 range0=len(number)
 list0=list(number)
 if range0 == 1:
  return units[int(number)+1]
 elif range0 == 2:
  if list0[0] == '1':
   return teens[int(list0[1])]
  else:
   if list0[1] != '0':
    first=dc[int(list0[0])-1]
    second=units[1:][int(list0[1])]
    if list0[0] == '2':
     return f"{first}{second}"
    else:
     return f"{first} y {second}"
   else:
    if list0[0] == '2':
     l='e'
    else:
     l='a'
    return dc[int(list0[0])-1][:-1] + l
 elif range0 == 3:
  last=''.join(list0[1:])
  if last == '00':
   return ctn[int(list0[0])]
  else:
   arr=''
   if list0[0] == '1':
    arr+='ciento'
   else:
    arr+=ctn[int(list0[0])]
   ax=list0[1:][0]
   if ax == '0':
    arr+=' ' + units[int(list0[-1])+1]
   if number[1:][0] == "0":
    return f"{arr}"
   else:
    if list0[0] != "1":
     return f"{ctn[int(number[0])]} {convert(number[1:])}"
    else:
     return f"ciento {convert(number[1:])}"
 elif range0 == 4:
  xm=f"{units[2:][int(number[0])-1]} mil "
  if number[1:] == "000":
   if number[0] == '1':
    return "Mil"
   else:
    return f"{units[2:][int(number[0])-1]} mil"
  else:
   if number[1:][0] == '0':
    tx=convert(number[2:])
    return f"{xm}{tx}"
   else:
    xt=convert(f"{number[1:]}")
    if number[0] == '1':
     return f"{xm.replace('uno', '')}{xt}"
    else:
     return f"{xm}{xt}"

def convert2(number):
 if not number.isdigit():
  return "El numero debe ser un valor numerico positivo."
 if int(number) <= 9999:
  return convert(number)
 blocks = []
 while number:
  blocks.insert(0, number[-3:])
  number = number[:-3]
 suffixes = ["", "mil", "millon", "mil millones", "billon"]
 result = []
 for i, block in enumerate(blocks):
  if int(block) != 0:
   text = convert(block.zfill(3))
   if i == len(blocks) - 1:
    result.append(text)
   else:
    if suffixes[len(blocks) - i - 1] == "millon" and int(block) == 1:
     result.append(f"{text} {suffixes[len(blocks) - i - 1]}")
    else:
     result.append(f"{text} {suffixes[len(blocks) - i - 1]}{'es' if suffixes[len(blocks) - i - 1] == 'millon' and int(block) > 1 else ''}")
 return " ".join(result).strip()


banner()
try:
 while True:
  number=input(' [*] INTRODUZCA EL NUMERO => ')
  if len(number) <= 4:
   print(f' ===> El "{number}" se escribe => ' + convert(number).strip())
  else:
   print(f' ===> El "{number}" se escribe => ' + convert2(number))
  input()
except ValueError:
 print(' Error, introduzca un numero')
except KeyboardInterrupt:
 print("\nHasta la proxima")




