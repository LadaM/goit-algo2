## Task 1
[task-1.py](task-1.py)

### Flow between terminals and stores

| Terminal   | Store    | Actual Flow |
|------------|----------|:-----------:|
| Terminal 1 | Store 1  |     15      |
| Terminal 1 | Store 2  |     10      |
| Terminal 1 | Store 3  |     20      |
| Terminal 1 | Store 4  |     15      |
| Terminal 1 | Store 5  |     10      |
| Terminal 1 | Store 6  |     20      |
| Terminal 1 | Store 7  |     15      |
| Terminal 1 | Store 8  |     15      |
| Terminal 1 | Store 9  |     10      |
| Terminal 1 | Store 10 |      0      |
| Terminal 1 | Store 11 |      0      |
| Terminal 1 | Store 12 |      0      |
| Terminal 1 | Store 13 |      0      |
| Terminal 1 | Store 14 |      0      |
| Terminal 2 | Store 1  |      0      |
| Terminal 2 | Store 2  |      0      |
| Terminal 2 | Store 3  |      0      |
| Terminal 2 | Store 4  |     10      |
| Terminal 2 | Store 5  |     10      |
| Terminal 2 | Store 6  |     10      |
| Terminal 2 | Store 7  |     15      |
| Terminal 2 | Store 8  |     15      |
| Terminal 2 | Store 9  |     10      |
| Terminal 2 | Store 10 |     20      |
| Terminal 2 | Store 11 |     10      |
| Terminal 2 | Store 12 |     15      |
| Terminal 2 | Store 13 |      5      |
| Terminal 2 | Store 14 |     10      |

1. Які термінали забезпечують найбільший потік товарів до магазинів?
   - Terminal 1 is capable of delivering goods to stores 1–9 up to their maximum capacity. It doesn't deliver to stores 10–14.
   - Terminal 2 delivers goods to stores 4-14, but for stores S4, S6, and S7 it cannot deliver up to the maximum capacity, therefore they will be better supplied from the terminal 1. From this terminal, there are no flows to stores 1-3.
   - Since Terminal 1 can deliver to 8 stores at maximum capacity, Terminal 2 only to 7, it can be said that terminal 1 supplies more stores at higher capacity and thus provides more overall flow.

2. Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік?
   - The routes from terminal 1 to stores 10–14 have zero flow.
   - The routes from terminal 2 to stores 1–3 have zero flow and do not contribute to the network.
   - The flow to the store 13 is only 5, which is less than all other stores.

3. Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів?
   - Only stores 6 and 7 receive fewer goods than they are capable of. They are attached to warehouses 2 and 3 which are supplied by both terminals.
   - Increasing the flows to W2 and W3 can resolve this issue.
   
4. Чи є вузькі місця, які можна усунути для покращення ефективності логістичної мережі?
   - Currently, all stores except 6 and 7 are supplied to their fullest capacity by the network
   - The network can be improved by increasing capacity of the flow to the warehouses 2 and 3

## Task 2
[task-2.py](task-2.py)

* Number of items: 100000
* Total range_query time for OOBTree: 0.000242 seconds
* Total range_query time for Dict: 0.533428 seconds

The OOBTree works much faster than default dictionary. Therefore, it has a lower time complexity.