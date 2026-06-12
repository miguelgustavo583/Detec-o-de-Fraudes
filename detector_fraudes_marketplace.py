from datetime import datetime

# ==========================
# BASE DE DADOS SIMULADA
# ==========================

usuarios = [
    {
        "id": 1,
        "nome": "João",
        "quantidade_comprada": 120,
        "preco_total": 6000,
        "cupom_valido": True
    },
    {
        "id": 2,
        "nome": "Maria",
        "quantidade_comprada": 90,
        "preco_total": 4500,
        "cupom_valido": True
    },
    {
        "id": 3,
        "nome": "Carlos",
        "quantidade_comprada": 600,
        "preco_total": 3000,
        "cupom_valido": False
    }
]

# ==========================
# CONFIGURAÇÕES
# ==========================

MEDIA_COMPRAS = 100
LIMITE_ANOMALIA = MEDIA_COMPRAS * 3

# ==========================
# FUNÇÕES
# ==========================

def enviar_alerta(usuario, motivo):
    print("\n[ALERTA]")
    print(f"Usuário: {usuario['nome']}")
    print(f"Motivo: {motivo}")
    print("Administrador notificado.\n")


def bloquear_conta(usuario):
    print(f"Conta de {usuario['nome']} bloqueada temporariamente.\n")


def registrar_log(usuario, motivo):
    with open("logs_fraudes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{datetime.now()} | "
            f"Usuário: {usuario['nome']} | "
            f"Motivo: {motivo}\n"
        )


def verificar_fraude(usuario):

    motivos = []

    if usuario["quantidade_comprada"] > LIMITE_ANOMALIA:
        motivos.append(
            f"Quantidade comprada ({usuario['quantidade_comprada']}) acima do esperado"
        )

    preco_unitario = (
        usuario["preco_total"] /
        usuario["quantidade_comprada"]
    )

    if preco_unitario < 20:
        motivos.append(
            f"Preço unitário suspeito: R${preco_unitario:.2f}"
        )

    if not usuario["cupom_valido"]:
        motivos.append("Cupom expirado ou inválido")

    return motivos


for usuario in usuarios:

    motivos = verificar_fraude(usuario)

    if motivos:

        motivo_completo = " | ".join(motivos)

        enviar_alerta(usuario, motivo_completo)
        bloquear_conta(usuario)
        registrar_log(usuario, motivo_completo)

    else:
        print(
            f"{usuario['nome']} - comportamento normal."
        )

print("\nVerificação concluída.")
