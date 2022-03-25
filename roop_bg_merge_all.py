import os
import subprocess

#os.system("bash bg_merge_all.sh")

path="data/demo_results"
files = os.listdir(path)


for filename in files:
    #print(filename)
    tmp_path = os.path.join(path,filename)
    #print(tmp_path)
    os.rename(tmp_path,"generated_result.png")
    os.system("bash bg_merge_all.sh")

    outdir = os.path.join("results",filename)
    os.rename("bg_merge/output.png", outdir)
    
    

