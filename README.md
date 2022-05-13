# CeneoScraper

## struktura opinii w serwisie  [ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item <br> div\[class$=positives\] ~ div.review-feature__item<br> div.review-feature__col:has(> div\[class$=positives\]) > div.review-feature__item|pros||
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item <br> div\[class$=negatives\] ~ div.review-feature__item<br> div.review-feature__col:has(> div\[class$=negatives\]) > div.review-feature__item|cons||
|dla ilu osób przydatna|span\[id^=votes-yes\]<br>button.vote-yes > span<br>button.vote-yes["data-total-vote"]|useful||
|dla ilu osób nieprzydatna|span\[id^=votes-no\]<br>button.vote-no > span<br>button.vote-no["data-total-vote"]|useless||
|data wystawienia mopinii|span.user-post__published > time:nth-child(1)\["datetime"\]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2)\["datetime"\]|purchase_date||


## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojednyczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku.json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwości podania kodu produktu przez użytkownika
7. Optymalizacja kodu
   a. utworzenie funkcji 
   b. utworzenie słownika selektorów
   c. użycie dictionary comprehension do pobrania składowych pojedynczej opinii na podstawie słownika selektorów
8. Analiza pobranych opinii dla konkretnego produktu
   a. wyliczenie podstawowych statystyk :
        - liczba wszystkich opinii
        - liczba opinii dla których podano zalety
        - liczba opinii dla których podano wady
        - średnia ocena produktu
   b. przygotowanie wykresów
        - udział poszczególnych rekomendacji w ogólnej liczbie opinii
        - histogram występowania poszczególnych ocen
<!--- review-feature__title review-feature__title--positives >

<!---   span[id^="votes-yes"]
        button.vote-yes > span
        button.vote-yes["data-total-vote"] <br>
        ?????


<!---  data wystawienia   span.user-post__published > time:nth-child(1)["datetime"]>
<!--- data zakupu ... (2)   >
