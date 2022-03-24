# bg_merge

```
docker run -it --name <NAME> --gpus '"device=0,1,2,3,4,5,6,7"' -v ~:/work --shm-size=2g shunyatoyokawa/masking:latest  bash
```


```
python main.py
```

背景画像と合成人物の切り抜きを入力にとる
