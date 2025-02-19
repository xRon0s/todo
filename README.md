# Color Checker

カラーチェッカーは**Pyside6**を用いたGUIアプリケーションで、**画像からのHEX,RGB値の取得機能**と**HEX値を用いた4つの色の比較機能**という2つの機能を持っています。この機能によりWEBデザインやロゴデザインに貢献することができます。
![全体](readme/スクリーンショット%202025-02-19%20181000.png)

## Features

- **カラーピックの機能**: 
  Load Imageより読み込んだ画像上（Jpg,Jpeg対応、png非対応）にマウスカーソルを当てることで画像上の色に対応したRGB値、HEX値を取得することができます。
 ![カラーピック](readme/スクリーンショット%202025-02-19%20184055.png)
  
- **色比較の機能**: 
  下部の4つの入力ボックスにHEX値（「#OOOOOO」　形式）を入力することで色を表示し、最大4種類の色を表示、比較することができます。
  ![色比較](readme/スクリーンショット%202025-02-19%20184200.png)

## Requirements

以下のPythonパッケージを含んでいます:

- PySide6==6.8.1.1
- numpy==2.2.0
- pillow==11.0.0
- python-dateutil==2.9.0.post0
- pyttsx3==2.98
- pywin32==308
- pywinpty==2.0.14
- PyYAML==6.0.2
- webcolors==24.11.1

## Installation

1. **リポジトリのクローン**:

    ```bash
    git clone https://github.com/xRon0s/todo.git
    cd todo
    ```

2. **仮想環境の構築**:

    ```bash
    python -m venv venv
    ```

3. **仮想環境のアクティブ化**:

  
      ```bash
      venv\Scripts\activate
      ```

4. **requirements.txtに記されたパッケージのインストール**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **立ち上げ方**:

    ```bash
    python main.py
    ```

2. **画像の読み込み方法**:
   - ウィンドウ上部に表示されているLoad Imageボタンを押して、PC内の画像を選択することで画像を読み込み、表示することができます（pngも読み込めますが透過部分で上手く作動しないことがあります）

3. **カラーピック方法**:
   - 読み込んだ画像上にマウスを持って行くとマウスの状態が（Pointer）になります。Pointer状態で画像のRGB値、HEX値を自動で取得し、表示してくれます。

4. **色比較の方法**:
   - 1~4個のHEX値（#を含めて7文字）を入力欄に入力します
   - 入力することで自動でHEX値に対応した色が表示されます（ 色が表示されない場合は下のCompareボタンを押すことで改善されます）