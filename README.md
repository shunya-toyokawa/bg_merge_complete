# bg_merge_complete

## 環境
```
docker run -it --name <NAME> --gpus '"device=0,1,2,3,4,5,6,7"' -v ~:/work --shm-size=2g shunyatoyokawa/masking:latest  bash
```
## 実行はこれだけ(入力はapp_root/data/origin.pngに元画像、app_root/data/demo_resultsにfake画像のデータセットを置けばいい)


```
python roop_bg_merge_all.py
```
