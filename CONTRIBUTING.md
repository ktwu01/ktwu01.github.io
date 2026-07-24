Contributions are welcome! 

Please add issues and make pull requests. There are no stupid questions. All ideas are welcome. This is a volunteer project. Be excellent to each other.

Bug reports and feature requests to the template  should be [submitted via GitHub](https://github.com/academicpages/academicpages.github.io/issues/new/choose). For questions concerning how to style the template, please feel free to start a [new discussion on GitHub](https://github.com/academicpages/academicpages.github.io/discussions).

Fork from master and go from there. Remember that this repository is intended to remain a generic, ready-to-fork template that demonstrates the features of academicpages.

## Blog URLs and translations

Blog permalinks follow one strict public format:

- English: `/posts/YYYY/MM/topic-slug/`
- Chinese: `/zh/posts/YYYY/MM/topic-slug/`

Translated versions must use the same `YYYY/MM/topic-slug`. Do not add `-en`, `-cn`, or `-zh` to a public permalink. Source filenames may retain a language marker such as `-cn.md`.

After adding, removing, or renaming a translated post, regenerate the automatic language navigation:

```bash
python3 scripts/generate_language_links.py
```

Author notes are generated from each post's explicit `lang` value when present,
then from its canonical permalink language. Do not write or edit them manually:

```bash
python3 scripts/generate_author_notes.py
```

Before opening a pull request, run the same checks as CI:

```bash
python3 scripts/generate_author_notes.py --check
python3 scripts/lint_blog_format.py
python3 scripts/generate_language_links.py --check
python3 -m unittest discover -s tests -v
```
