import json

def fazer_onboarding():
    """Coleta informações iniciais do aluno"""
    print("=" * 50)
    print("🎓 BEM-VINDO AO AIZEN - SEU TUTOR DE VESTIBULAR")
    print("=" * 50)
    print()
    
    # Coleta dados básicos
    nome = input("Qual seu nome? ")
    vestibular = input("Qual vestibular você vai fazer? (ex: UEA 2026) ")
    idade = int(input("qual sua idade?"))
    
    # Lista de matérias do vestibular UEA
    materias = [
        "Matemática",
        "Português",
        "Física",
        "Química",
        "Biologia",
        "História",
        "Geografia",
        "Inglês",
        "redação"
    ]
    
    print("\n" + "=" * 50)
    print("Avalie seu nível em cada matéria (1 a 5):")
    print("1 = Muito fraco | 5 = Muito forte")
    print("=" * 50)
    
    avaliacoes = {}
    
    for materia in materias:
        while True:
            try:
                nota = int(input(f"\n{materia}: "))
                if 1 <= nota <= 5:
                    avaliacoes[materia] = nota
                    break
                else:
                    print("❌ Por favor, digite um número entre 1 e 5")
            except ValueError:
                print("❌ Por favor, digite um número válido")
    
    # Monta o dicionário completo do aluno
    dados_aluno = {
        "nome": nome,
        "vestibular": vestibular,
        "avaliacoes": avaliacoes
    }
    
    # Salva em arquivo JSON
    with open("aluno.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados_aluno, arquivo, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 50)
    print("✅ Perfil salvo com sucesso!")
    print("=" * 50)
    
    return dados_aluno


def mostrar_resumo():
    """Lê o JSON e mostra um resumo do perfil do aluno"""
    try:
        with open("aluno.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        print("\n" + "=" * 50)
        print(f"📊 PERFIL: {dados['nome'].upper()}")
        print("=" * 50)
        print(f"🎯 Vestibular: {dados['vestibular']}")
        print("\n📚 Suas avaliações:")
        
        # Organiza por nota (menor para maior)
        materias_ordenadas = sorted(
            dados['avaliacoes'].items(), 
            key=lambda x: x[1]
        )
        
        for materia, nota in materias_ordenadas:
            # Cria barra visual
            barra = "█" * nota + "░" * (5 - nota)
            print(f"  {materia:12} [{barra}] {nota}/5")
        
        # Identifica pontos fracos (nota <= 2)
        pontos_fracos = [
            materia for materia, nota in dados['avaliacoes'].items() 
            if nota <= 2
        ]
        
        # Identifica pontos fortes (nota >= 4)
        pontos_fortes = [
            materia for materia, nota in dados['avaliacoes'].items() 
            if nota >= 4
        ]
        
        print("\n" + "=" * 50)
        
        if pontos_fracos:
            print("⚠️  FOCAR EM:")
            for materia in pontos_fracos:
                print(f"   • {materia}")
        
        if pontos_fortes:
            print("\n💪 SEUS PONTOS FORTES:")
            for materia in pontos_fortes:
                print(f"   • {materia}")
        
        # Calcula média geral
        media = sum(dados['avaliacoes'].values()) / len(dados['avaliacoes'])
        print(f"\n📈 Média geral: {media:.1f}/5")
        print("=" * 50)
        
    except FileNotFoundError:
        print("\n❌ Erro: Arquivo aluno.json não encontrado!")
        print("Execute o onboarding primeiro.")


def main():
    """Função principal"""
    print("\n🤖 Iniciando Aizen...\n")
    
    # Faz o onboarding
    fazer_onboarding()
    
    # Mostra o resumo
    mostrar_resumo()


# Executa o programa
if __name__ == "__main__":
    main()