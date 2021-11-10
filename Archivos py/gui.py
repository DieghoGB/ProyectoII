from funciones import *



#video
lblVideo.grid(column=1, row=0)

#info
infoTextoLBL.grid(column=2, row = 0)

#boton
escanearTexto.set("Escanear")
escanearBtn = tkinter.Button(root, textvariable = escanearTexto,bg = "#20bebe",
                             fg = "white", height = 2, width = 15, command=escanear)

escanearBtn.grid(column = 1, row = 2)

iniciar()
root.mainloop()