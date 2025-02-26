import tkinter as tk
from tkinter import simpledialog

def obter_lista():
   # Função para processar os valores inseridos
    def processar_valores():
        
        item_counts = {}
        duplicates = []
        
        resposta = entry.get("1.0", tk.END) # Obtém o texto inserido
        if resposta:
            lista = resposta.split()  # Divide a string em uma lista
        # Iterate over the list
            for item in lista:
                # If the item is already in the dictionary, it's a duplicate
                if item in item_counts:
                    duplicates.append(item)
                        # Otherwise, add it to the dictionary with a count of 1
                else:
                    item_counts[item] = 1
            
            if duplicates:
                exibe_duplicados(duplicates,lista)
            else:
                exibe_mensagem() 
           
    
    def exibe_duplicados(duplicates,lista):
        
        lista_sem_duplicatas = list(set(lista))
     
        sem_resultado.pack_forget()
        resultado_duplicado.delete(1.0, tk.END)  # Limpa o campo de saída antes de atualizar
        resultado_nao_duplicado.delete(1.0, tk.END) 
        resultado_duplicado.insert(1.0,"\n".join(duplicates))
        resultado_nao_duplicado.insert(1.0,"\n".join(lista_sem_duplicatas))
        resultado_label_duplicado.pack()
        resultado_duplicado.pack()
        resultado_label_nao_duplicado.pack()
        resultado_nao_duplicado.pack()
        
    def exibe_mensagem():
        resultado_duplicado.pack_forget()
        resultado_nao_duplicado.pack_forget()
        resultado_label_duplicado.pack_forget()
        resultado_label_nao_duplicado.pack_forget()
        sem_resultado.pack()
        sem_resultado.config(text=f"Não há itens duplicados")  

    root = tk.Tk()
    root.title("Verifica duplicada")

    # Cria um rótulo de instrução
    instrucao_label = tk.Label(root, text="Insira os valores que serão analisados:")
    instrucao_label.pack(pady=10)

    # Cria um campo de texto para entrada
    entry = tk.Text(root, width=50, height=10)
    entry.pack(pady=5)

    # Botão para processar a entrada
    button = tk.Button(root, text="Mostrar Lista", command=processar_valores)
    button.pack(pady=5)

    # Rótulo para mostrar sem resultado
    sem_resultado= tk.Label(root, text="")
    sem_resultado.pack(pady=5)
    
    resultado_label_duplicado = tk.Label(root, text="Itens duplicados:")
    
    resultado_duplicado = tk.Text(root, width=50, height=10)

    resultado_label_nao_duplicado = tk.Label(root, text="Itens exclusivos:")
    
    resultado_nao_duplicado = tk.Text(root, width=50, height=10)
    
    # Definir largura x altura + posição X + posição Y
    root.geometry("600x800+100+0")  # Largura=600, Altura=400, Posição X=100, Posição Y=100
    
    # Exibe a janela
    root.mainloop()

obter_lista()
