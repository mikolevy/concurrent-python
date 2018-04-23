# concurrent-python
Code examples and exercises for beIT conference workshop

In slides.pdf file you can find slides from the presentation (in Polish only). Below my notes for the workshop (in Polish only)


## Notes

- basic_example.py -> Przykład użycia modułu threading
- exercise_1.py -> Przerobić liczenie królików na wielowątkowe
- solution_1.py -> Proste, błędne rozwiązanie, wyścig na zmiennej  globalnej oraz funkcji print -> ale wszystko wydaje się być ok gdy uruchamiamy program - dlaczego?
- exercise_2 -> Program wielowątkowy jest niedeterministyczny, wątki mogą wykonywać się w różnej kolejności. Dodając losowe opóźnienia możemy zwiększyć szansę na wystąpienie błędów spowodowanych wyścigami. Program nie działa poprawnie. Aby go poprawić wykorzystamy kolejki.
- queue_example -> Kolejka pozwala zarządzać dostępem do zasobów współdzielonych. Dobrą regułą jest upewnienie się, że tylko jeden wątek ma dostęp do zasobu współdzielonego. Żądanie związane z tym zasobem może zostać przekazane do niego właśnie poprzez kolejkę
- exercise_2 -> Usuwamy wyścigi - należy przerobić program, tak aby korzystał z modułu queue.
- solution_2 -> Rozwiązanie problemu liczenia królików z wykorzystaniem dwóch kolejek. Jeden wątek ma dostęp do współdzielonego zasobu liczby królików, a drugi do wypisywania na ekran
- solution_2_no_fuzzy -> "Wyczyszczony" przykład rozwiązania problemu liczenia królików

To nie takie trudne! A jednak...
- queue_example_hang -> Jeżeli zapomnimy o drobnym szczególe, np. tasks_queue.task_done() program działa ale... zawiesza się!
- lock_example.py -> Locki, przykład wygląda ładnie i czysto (pięknie dzięki with!)
- exercise_3 -> Przerobić program tak by korzystał z locków
- solution_3 -> Program z lockami działa poprawnie
- solution_3_no_fuzzy -> Jest krótszy i bardziej czytelny od wersji z kolejkami. Jest też deterministyczny -> nic w nim nie wykonuje się współbieżnie

Problemy z lockami:
- Locki niczego nie lockują (locks_mean_example) -> dodając nowy kod możemy popsuć stary
- Bardzo trudno jest dodać odpowiednią liczbę locków w złożonym programie, a błędy są trudne do wykrycia
- Wydajnością porównywalne z queue

Wątki w Pythonie a wzrost wydajności
- exercise_cpu -> wymagające obliczeniowo zadanie, należy skrócić czas wykonania stosując threading
- solution_threading -> uruchamiając obliczenia w wielu wątkach program wykonuje się tyle samo czasu lub nawet wolniej!

Przyczyną jest GIL

- multiprocessing -> aby wykorzystać dodatkowe rdzenie w Pythonie stosujemy moduł multiprocessing. Przerobić program solution_threading tak by korzystał z wielu procesów
- solution_multiprocessing -> Program wykonuje się dużo szybciej! Składnia bardzo zbliżona do wątków (w multiprocessing również mamy queue i locki).

Ile procesów uruchomić? Jeżeli program jest wymagający dla CPU to liczba rdzeni logicznych (zazwyczaj liczba rdzeni fizycznych x 2) stanowi dobry punkt wyjścia. Im więcej operacji IO tym więcej procesów można utworzyć. Odpowiednią liczbę należy odkryć poprzez eksperymenty!

Czy wątki nie nadają się do niczego?
- io_intensive: exercise -> Program, który wykonuje głównie operacje IO (np. pobiera dane z internetu). W trakcie pobierania danych, odczytu z dysku itp. procesor czeka -> potencjał dla wątków! Przerobić program tak by korzystał z wątków
- solution_threading -> Program działa prawie 10x szybciej! Kiedy wątek czeka (na dane, śpi itp.) interpreter Pythona przełącza wykonanie do innego wątku. W ten sposób wszystkie 10 wątków czeka na dane w tym samym czasie

- Porównanie multiprocessing vs threading (slajdy)
- Prawo Amdhala (slajdy)

- async_example -> Omówienie programu. Porównanie z modelem threading (slajdy).
- async_exercise -> przerobić program na wersję asynchroniczną
- async_solution/async_solution_2 -> rozwiązanie działa dużo szybciej. Prosty kod, mała szansa popełnienia błędu ale... wszystko musi być async!
