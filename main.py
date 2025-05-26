from utils.validation import is_ip, is_domain, is_url, is_hash
from apis.virustotal import enrich_ip, enrich_domain, enrich_url, enrich_hash

def mostrar_resultado(dados):
    try:
        atributos = dados.get("data", {}).get("attributes", {})
        if not atributos:
            print("Nenhum dado retornado.")
            return

        print("\n--- Resultado do Enriquecimento ---")
        for chave, valor in atributos.items():
            if isinstance(valor, (str, int, float)):
                print(f"{chave}: {valor}")
    except Exception as e:
        print("Erro ao interpretar resultado:", e)

def main():
    entrada = input("Digite um IP, domínio, url ou hash: ").strip()

    if is_ip(entrada):
        tipo = "ip"
        dados = enrich_ip(entrada)
    elif is_domain(entrada):
        tipo = "domain"
        dados = enrich_domain(entrada)
    elif is_url(entrada):
        tipo = "url"
        dados = enrich_url(entrada)
    elif is_hash(entrada):
        tipo = "hash"
        dados = enrich_hash(entrada)
    else:
        print("Entrada inválida.")
        return

    print(f"\nTipo detectado: {tipo}")
    mostrar_resultado(dados)

if __name__ == "__main__":
    main()
