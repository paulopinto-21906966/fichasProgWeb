import os


def pede_pasta():
    while not os.path.isdir(input("Insira um caminho para a pasta: ")):
        print("experimente " + os.getcwd())

    return True


def faz_calculos():
    files = os.listdir()
    filesTuples = list([file.split(".") for file in files if "." in file])
    print(filesTuples)
    # print({extension: filename for filename, extension in filesTuples})

    fileDict = dict()

    for filename, extension in filesTuples:
        if extension in fileDict:
            fileDict[extension] += os.path.getsize(filename) / 2 ** 10
        else:
            fileDict[extension] = os.path.getsize(filename) / 2 ** 10
    print(fileDict)

    # print(dict((file.split("."), file.split(".")) for file in files))
    # filesDict = dict(file.split(".") for file in files if "." in file)
    # for file in files:
    #
    #     data = file.split(".")
    #     print(data)
    #     if len(data) == 2:
    #         dict[data[1]] = data[0]
    #         print(data)
    #
    #     peso += os.path.getsize(file) / 2 ** 10;
    # print(filesDict)
    # print(str(peso) + "kb")
    # print(filesDict)
