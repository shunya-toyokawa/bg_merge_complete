


#masking (app_root/data/origin.png)
python3 masking.py 


cp masked.png inpaint/masked.png

cp data/origin.png inpaint/origin.png

cd inpaint
#inpaint (app_root/inpaint/masked.png, app_root/data/origin.png)
python3 inpaint.py


cd ..



#masking generated_result(ganで生成した画像)

cp -f generated_result.png origin.png
python3 masking_fake.py 

rm bg_merge/cutout.png
ls bg_merge
cp -f cutout.png bg_merge/cutout.png

mv -f inpaint/inpaint.png bg_merge/inpaint.png



#merge
cd bg_merge


python3 main.py


cd ..

