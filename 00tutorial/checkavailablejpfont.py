# https://beiznotes.org/matplotlib-toufu/
import logging

import matplotlib.font_manager as fm
from fontTools.ttLib import TTCollection, TTFont

logging.getLogger("fontTools").setLevel(logging.ERROR)


def get_japanese_supported_families(font_path, test_char="あ"):
    """
    指定したフォントファイル内で、テスト文字に対応しているフォントの
    ファミリ名のリストを返す（TTCollectionにも対応）。
    """
    families = []
    try:
        # TTC/OTCの場合はコレクションとして読み込み、それ以外はTTFontで読み込み
        if font_path.lower().endswith((".ttc", ".otc")):
            collection = TTCollection(font_path)
            fonts = collection.fonts
        else:
            fonts = [TTFont(font_path)]

        for font in fonts:
            # cmapテーブルをチェックし、テスト文字が含まれているか確認
            has_japanese = False
            for table in font["cmap"].tables:
                if table.isUnicode() and ord(test_char) in table.cmap:
                    has_japanese = True
                    break
            if not has_japanese:
                continue

            # nameテーブルからファミリ名（nameID=1）を取得
            family_name = None
            for record in font["name"].names:
                if record.nameID == 1:
                    try:
                        family_name = record.string.decode(record.getEncoding())
                    except Exception:
                        family_name = record.string.decode("utf-8", errors="replace")
                    break
            if family_name:
                families.append(family_name)
            else:
                families.append("不明")
    except Exception:
        return []
    return families


# システムにあるフォントのパス一覧を取得
system_fonts = fm.findSystemFonts()

# 各フォントファイルについて、日本語対応かつファミリ名が取得できるものを抽出
font_info = []
for font in system_fonts:
    families = get_japanese_supported_families(font)
    if families:
        font_info.append((font, families))

print("日本語対応フォント:")
for path, families in font_info:
    print(f"{', '.join(families)} : {path}")
