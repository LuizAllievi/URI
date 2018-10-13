N1, N2, N3, N4 = map(float, input().split())

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10



if (media >= 7):
    msg = "Aluno aprovado."
elif (media < 5):
    msg = "Aluno reprovado."
else:
    msg = "Aluno em exame."
    exame = float(input())
    final = (media + exame) / 2

    msg += "\nNota do exame: {:.1f}".format(exame)

    if (final >= 5):
        msg += "\nAluno aprovado."
    else:
        msg += "\nAluno reprovado."

    msg += "\nMedia final: {:.1f}".format(final)
print("Media: {:.1f}".format(media))
print(msg)
