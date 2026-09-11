
#progama de calculo de desconto

#DEFINIÇÃO DO VALOR DA COMPRA
vc = float(input("DIGITE O VALOR DA COMPRA:"))

#CONDIÇÕES PARA OS VALORES DAS COMPRAS PARA INSERIR OS DESCONTOS 
if vc < 200 :
   #CONTAS DO DESCONTO
   d5= vc*0.95
   vd5= vc-d5

   #EXIBIÇÃO DOS RESULTADOS
   print("desconto de 5%")
   print(f"Valor do desconto: {vd5}")
   print(f"Total a pagar: {d5}")
   
else :
   if vc >= 200 and vc < 300 :
     #CONTAS DO DESCONTO
     d10= vc*0.90
     vd10= vc-d10

     #EXIBIÇÃO DOS RESULTADOS
     print ("desconto de 10%")
     print(f"Valor do desconto: {vd10}")
     print(f"Total a pagar: {d10}")
     
   else :
       if vc >= 300 :
        #CONTAS DO DESCONTO
        d15= vc*0.85
        vd15= vc-d15

        #EXIBIÇÃO DOS RESULTADOS
        print ("desconto de 15%")
        print(f"Valor do desconto: {vd15}")
        print(f"Valor da compra: {d15}")
        
