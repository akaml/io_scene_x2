For personally customizing and using, this addon was forked from official
DirectX X format exporter(https://github.com/cdbfoster/io_scene_x).

## Modification
- DirectX9 becomes unable to read a model file which includes "Sword", or "sword" in material name.
For that reason, Modify to output the readable file. 
- In DirectX9, 1 second is 4800 frame, if there are 60 key frames in 1 second, it's necessary to increase 80 frames each 1 key frame.
This doesn't matter at 32bit DirectX, but it matters at 64bit(At the above example, it is played with 80 times.).
Therefore, change to output after (4800 / key frame number per 1 second) times.
- In original edition, Blender rendering settings was used as animation length, so that all animation was output same length.
I wanted to change length each animation, change to output while individual animation last key frame as animation length. 
- In original edition, it couldn't save output settings, so that it was fixed.
With this change, output settings moved from the screen like file explorer to addon settings screen.
- In original edition, a model of not having bone can only output one animation that is playing now, on the other hand,
a model of having bone have output all animation in Scene. I wanted to register animation each a model,
so that I modified to output animations to be registered in NLA Track.
### NOTE:
- Output is very slow. This is due to the "bpy.context.scene.frame_set" method.
It solves if modify to create new scene, paste only target model and output it.

## 変更点
- "Sword"、もしくは"sword"という名前のマテリアルを含んだモデルを出力するとDirectXが読み込めなくなるので、
読み込めるファイルを出力するように修正。
- DirectX9では1秒は4800フレームなので1秒に60個のキーフレームがある場合、1キーフレームごとに80フレーム増加する必要がある。
これは32bit版のDirectXでは問題にならないが、64bit版では問題となる。(上記の例では80倍で再生されてしまう)
このためフレームを(4800/1秒あたりのキーフレーム数)倍にして出力するようにした。
- オリジナル版ではアニメーションの長さとしてBlenderのレンダリング設定が使用されており、
すべてのアニメーションが同じ長さで出力される。
アニメーションごとに長さを変更したかったので、
個々のアニメーションの最後のキーフレームまでをアニメーションの長さとして出力するように変更した。
- オリジナル版では出力設定を保存できなかったため、保存できるようにした。
これに伴い、出力設定はファイルエクスプローラ風画面からアドオン管理画面に移動した。
- オリジナル版では骨のないモデルは現在再生中のアニメーション1つしか出力されず、
一方で骨のあるモデルはシーン内のすべてのアニメーションを出力するようになっていた。
モデルごとに出力したいアニメーションを登録したかったので
NLA Trackに登録されているアニメーションを出力するように変更した。
### 備考
- 出力がとても遅いが、これはbpy.context.scene.frame_setメソッドが原因である。
  シーンを新規作成して、出力対象のモデルだけを貼り付けて出力するように修正すれば解決する。
