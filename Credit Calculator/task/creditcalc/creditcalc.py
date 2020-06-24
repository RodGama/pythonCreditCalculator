import math
import sys

args = sys.argv
acao = ""
tipo = ""
credit = ""
mensalidade = ""
interest = ""
meses = ""

for arg in args:
    if arg.__contains__("--type="):
        acao = arg.replace("--type=", "")
    if len(args) < 4:
        print("Incorrect parameters")
        exit()

    if arg.__contains__("--principal="):
        credit = arg.replace("--principal=", "")
    elif arg.__contains__("--interest="):
        interest = arg.replace("--interest=", "")
    elif arg.__contains__("--payment="):
        mensalidade = arg.replace("--payment=", "")
    elif arg.__contains__("--periods="):
        meses = arg.replace("--periods=", "")
if acao == "diff":
    if interest == "":
        print("Incorrect parameters")
        exit()
    interest = float(interest)
    credit = int(credit)
    meses = int(meses)
elif acao == "annuity" and len(args) < 5:
     print("Incorrect parameters")
     exit()
else:
    if credit == "":
        tipo = "credito"
        interest = float(interest)
        mensalidade = int(mensalidade)
        meses = int(meses)
    elif meses == "":
        tipo = "periodo"
        interest = float(interest)
        mensalidade = int(mensalidade)
        credit = int(credit)
    elif mensalidade == "":
        tipo = "mensalidade"
        interest = float(interest)
        credit = int(credit)
        meses = int(meses)

if acao == "annuity":
    if tipo == "periodo":
        interest = (interest / 100) / 12
        interest_log = math.log(1 + interest)
        m_denominador = mensalidade - interest * credit
        mensalidade_calc_para_log = mensalidade / m_denominador
        mensalidade_log = math.log(mensalidade_calc_para_log, math.e)
        parcelas = math.ceil(mensalidade_log / interest_log)
        meses = math.ceil(parcelas)
        if parcelas // 12 > 1:
            anos = parcelas // 12
            if anos > 1:
                anos_aux = str(anos) + " years"
            if parcelas % 12 != 0 and parcelas % 12 > 1:
                anos_aux += " and " + str(parcelas % 12) + " months"
            elif parcelas % 12 != 0 and parcelas % 12 == 1:
                anos_aux += " and " + str(parcelas % 12) + " month"
            print(f"It takes {anos_aux} to repay the credit")
        else:
            if parcelas % 12 != 0 and parcelas % 12 > 1:
                anos_aux = str(parcelas % 12) + " months"
            elif parcelas % 12 != 0 and parcelas % 12 == 1:
                anos_aux = str(parcelas % 12) + " month"
            print(f"It takes {anos_aux} to repay the credit")
    elif tipo == "mensalidade":
        interest = (interest / 100) / 12
        anuidade = credit * ((interest * ((1+interest)**meses)) / (((1+interest)**meses) - 1))
        mensalidade = math.ceil(anuidade)
        print(f"Your annuity payment = {math.ceil(anuidade)}!")
    elif tipo == "credito":
        interest = (interest / 100) / 12
        credit = int(mensalidade/((interest * ((1+interest)**meses)) / (((1+interest)**meses) - 1)))
        print(f"Your credit principal = {math.floor(credit)}!")

    overpay = abs(mensalidade * meses - credit)
    print("")
    print("Overpayment = {}".format(overpay))
elif acao == "diff":
    interest = (interest / 100) / 12
    pagamento = 0
    anuidade = credit * ((interest * ((1+interest)**meses)) / (((1+interest)**meses) - 1))
    for m in range(1, meses+1):
        diferencial = math.ceil((credit / meses) + (interest * (credit - ((credit * (m-1))/meses))))
        pagamento = pagamento + diferencial
        print(f"Month {m}: paid out {int(diferencial)}")

    print(f"\nOverpayment = {abs(credit - pagamento)}")
    #  abs(mensalidade * meses - int(credit))
