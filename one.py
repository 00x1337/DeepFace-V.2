import glob
from deepface import DeepFace
from time import sleep
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']

txtfiles = []
#soon in v2
# for file in glob.glob("g\\*.*"):
#     r = file.replace("g\\" ,"")
#     obj = DeepFace.analyze(img_path = file, actions = ['age', 'gender', 'race', 'emotion'])
#     print(f"""
    
#     Around age : {obj["age"]}
#     Img     : {r}
#     Status  : {obj["dominant_emotion"]}
#     """
        
#         )

for file in glob.glob("g\\*.*"):
    try:

        r = file.replace("g\\" ,"")
        txtfiles.append(r)
        for file1 in glob.glob("g\\*.*"):
            r1 = file1.replace("g\\" ,"")
            if not file == file1:
            
                result  = DeepFace.verify(file,file1)
                rrw = result["verified"]
                rrw1 = result["distance"]
                if rrw == True or 0.4 >= rrw1:
                    if not r1 in txtfiles:
                        print(f" img [1] : {r}\n img [2] : {r1}\n verified : {rrw}\n distance : {rrw1}\n\n\n")
    except:
        pass