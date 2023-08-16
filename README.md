# WavGenerator
Speech generation from text based on Yandex SpeechKit.


## Installation guide:

- install 'pipenv'

`pip install pipenv`
- open the project directory:

`cd WavGenerator`
- create lock file:

`pipenv lock`
- install dependencies:

`pipenv install`

## User guide:

- WavGenerator.py uses argparse. For information about CL args use -h.
- Text for speech generation should be written in one file (default: text.txt) and used as -input flag from CL.
- Wav files would be generated in output_dir (default: wav/) that is set by -output_dir flag from CL.
- Every string in -input would be generated as separate files. Names of these files are set as the number of string in the -input file.

## NOTE: 
It is needed a Yandex Cloud API-key for the script running.
Use your own one or connect with script provider for the key obtaining.


## Элементы разметки {#markup-elements}

| Описание | Спецсимволы и теги |
|---|---|
| [Поставить ударение](#a) | `+` |
| [Явно указать паузу между предложениями](#pause) | `sil<[t]>`, где t — длительность паузы в миллисекундах. |
| [Указать паузу, зависящую от контекста](#context-pause) | `<[small]>`. Допустимые значения: `tiny`, `small`, `medium`, `large`, `huge` |
| [Выделить акцент](#accent) | `<[accented]>` или `**акцентное слово**` |
| [Использовать фонетическое произношение](#phoneme) | `[[ <фонемы слова, разделенные пробелами> ]]` |

### Поставить ударение {#a}

Используйте символ `+` перед ударной гласной, в случаях, когда нужно уточнить корректный вариант произношения слова, например:

```text
Дверь в комнату заперта на зам+ок.
```

или

```text
Вход в з+амок действительно существовал.
```

### Явно указать паузу между предложениями {#pause}

Для явного указания паузы между предложениями вы можете добавить специальный тег: `sil<[t]>`, где t — длительность паузы в миллисекундах:

```text
Унылая пора! sil<[300]> Очей очарованье!
```

{% note info %}

Текст для синтеза не может состоять только из символов разметки. С помощью {{ speechkit-name }} нельзя сгенерировать файл с тишиной вместо речи.

{% endnote %}

### Установить паузу, зависящую от контекста {#context-pause}

Используйте слова-подсказки, чтобы длительность пауз подбиралась автоматически.

```
Мороз и солнце; <[medium]> день чудесный!
```

### Выделить акцент {#accent}

Чтобы выделить акцент, можно использовать тег `<[accented]>` или выделить слово при помощи ``**accented**``. Например:

```text
Удобные интерфейсы для решения <[задач]>.
```

или

```text
Мы **всегда** будем в ответе за тех, кого приручили.
```

### Использовать фонетическое произношение {#phoneme}

Используйте выделение блоком `[[ ]]`, чтобы контролировать правильность произношения с помощью фонем. Для воспроизведения будет использован текст в блоке:

```text
Привет! Меня зовут [[v a sʲ ʌ]]
```
