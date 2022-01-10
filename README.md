# Python の Class でまるバツゲームを作る。

## 名詞抽出法でやる。

## ネットの力は使わない。

### 要件定義

1. 縦 3 マス横 3 マスの入力できる 9 マスを用意する
2. ２名のプレイヤーが交互に〇と ◆ をマスに入力する
3. 同じ図形（〇か ◆）が一列（縦・横・斜め）でも揃ったら勝ち
4. すべてのマスが埋まったら引き分け

### プログラミングの 3 大原則で考える。

1. 変数
   cal
   row
   masu
   player1
   player2
   maru
   batu
   retu_row
   retu_cal
   retu_naname
   win
   lose
   drow

2. 値
   cal = (1,2,3)
   row = (1,2,3)
   masu = [
   [(1,1), (1,2), (1,3)],
   [(2,1), (2,2), (2,3)],
   [(3,1), (3,2), (3,3)],
   ]
   player1 = 〇
   player2 = ◆
   retu_row
   retu_cal
   retu_naname
   hantei = [win, lose, drow]

3. 処理
   create_new_masu()
   wirte()
   hantei()

### 結果

あんまり設計通りにならなかった。
