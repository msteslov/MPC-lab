# MPC-lab

Небольшой учебный проект по confidential computing и secure multi-party computation.

Цель проекта — показать базовые механизмы MPC на Python: арифметику в конечном поле, additive secret sharing, Shamir secret sharing, Beaver triples и демонстрацию secure aggregation.

## Планируемая структура

```text
mpc-lab/
  README.md
  src/
    finite_field.py
    additive_sharing.py
    shamir.py
    beaver.py
    secure_aggregation.py
  tests/
  examples/
    secure_sum_demo.py
```

## Что будет реализовано

- Арифметика в конечном поле по модулю простого числа.
- Additive Secret Sharing.
- Shamir Secret Sharing.
- Восстановление секрета через интерполяцию Лагранжа.
- Умножение secret-shared значений с использованием Beaver triples.
- Demo secure aggregation для вычисления суммы или среднего без раскрытия индивидуальных входов.
