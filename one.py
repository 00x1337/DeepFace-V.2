import glob
from deepface import DeepFace
from time import sleep
import os
from numpy.lib.function_base import select
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']

txtfiles = []
class filter():

    def matched():
        all =[]
        numr = 0
        numg = 0
        try:
            for file in glob.glob("Photos\\*.*"):
                print(file)
                r = file.replace("Photos\\" ,"")
                txtfiles.append(r)
                for file1 in glob.glob("Photos\\*.*"):
                    r1 = file1.replace("Photos\\" ,"")
                    if not file == file1:
                    
                        result  = DeepFace.verify(file,file1)
                        rrw = result["verified"]
                        rrw1 = result["distance"] 
                        if rrw == True or 0.4 >= rrw1:
                            if not r1 in txtfiles:
                                all.append(f"""
                        IMG : {r}
                        --------
                        IMG 2 {r1}
                        --------
                        MODE : True
                        """)
                                numr +=1
                            else:
                                numg +=1
                        else:
                            numg +=1
                    else:
                        numg +=1
                    try:
                        os.system("cls")

                    except:
                        os.system("clear")
                    print(f"IMG : {str(numr)} | Not :{str(numg)} | MODE : matched")

                    print("\n\n".join(all))

        except:
            try:
                    os.system("cls")
            except:
                os.system("clear")
                
            print(f"IMG : {str(numr)} | Not :{str(numg)} | MODE : matched")

            print("\n\n".join(all))
            print(f"IMG : {str(numr)} | Not :{str(numg)} | MODE : matched")
            print("[+] Finished")

    

    def statas():

       
        mode_filter = ["age","dominant_race","dominant_emotion","gender"]
        list_of_modes =[]
        for ii in range(0,3):
            list_of_modes.append(mode_filter[ii]+f" [{str(ii)}]")
        print("[ + ]Select Mode \n"+ "\n".join(list_of_modes) +"\n")
        mode_selected = input()
        modes = {
            "0": "Enter Age >=\n",
            "1": ["white","black"],
            "2": ["angry","neutral","surprise","sad","happy","fear"],
            "3": ["Men","Woman"]
        }
        try:
            list_of_modes2 = []
            if not "0" == modes[str(mode_selected)]:

                for i in range(len(modes[str(mode_selected)])):
                    list_of_modes2.append(f"{modes[mode_selected][i]}  [{str(i)}] ")
                print("\n".join(list_of_modes2))

        except:
             pass
        FFe = input("")
        try:
            all = []
            numr = 0
            numg = 0
            for file in glob.glob("Photos\\*.*"):
                result  = DeepFace.analyze(file,actions = ['age', 'gender', 'race', 'emotion'])

                if result[mode_filter[int(mode_selected)]] == str(modes[str(mode_selected)][int(FFe)]):
                    all.append(f"""
                    IMG : {file}
                    --------
                    MODE : {result[mode_filter[int(mode_selected)]]}
                    
                    """)
                    numr +=1

                else:
                    numg +=1
                try:
                    os.system("cls")

                except:
                    os.system("clear")
                print(f"IMG : {str(numr)} | Not :{str(numg)} | MODE : statas")

                print("\n\n".join(all))
                
        except:
            try:
                    os.system("cls")
            except:
                os.system("clear")
                
            print(f"IMG : {str(numr)} | Not :{str(numg)} | MODE : statas")
            print("\n\n".join(all))
            print(f"IMG : {str(numr)} | Not :{str(numg)} | MODE : matched")
            print("[+] Finished")
    
    if __name__ == '__main__':
        print(" [1] matched \n [2] statas")
        ans = input("")
        if ans == "1":
            matched()
        elif ans == "2":
            statas()
        else:
            exit(0)

filter()
    
