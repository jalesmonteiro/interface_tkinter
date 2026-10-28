import tkinter as tk

class LampadaApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Lâmpada")
        self.janela.geometry("300x350")
        self.janela.config(bg="#f1f1f1")
        
        self.ligada = False
        
        self.rotulo_lampada = tk.Label(
            janela,
            text="DESLIGADA",
            font=("Arial", 16, "bold"),
            width=14,
            height=3,
            bg="#203030",
            fg="#5a6b82",
        )
        self.rotulo_lampada.pack(pady=40)
        
        self.botao_interruptor = tk.Button(
            janela,
            text="Acender",
            font=("Arial", 12, "bold"),
            bg="#3b82f6",
            fg="#ffffff",
            activebackground="#2563eb",
            activeforeground="#ffffff",
            padx=20,
            pady=10,
            command=self.alternar_estado
        )
        self.botao_interruptor.pack(pady=10)
        
    def alternar_estado(self):
        self.ligada = not self.ligada
        
        if self.ligada:
            self.rotulo_lampada.config(
                text="LIGADA",
                bg="#fef08a",
                fg="#854d0e"
            )
            self.botao_interruptor.config(
                text="Apagar",
                bg="#ef4444",
                activebackground="#dc2626"
            )
        else:
            self.rotulo_lampada.config(
                text="DESLIGADA",
                bg="#1e3030",
                fg="#5a6a8a"
            )
            self.botao_interruptor.config(
                text="Acender",
                bg="#3b82f6",
                activebackground="#2563eb"
            )
            
janela = tk.Tk()
aplicacao = LampadaApp(janela)
janela.mainloop()

