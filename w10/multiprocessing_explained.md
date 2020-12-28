Библиотека multiprocessing позволяет организовать параллелизм вычислений за счет создания подпроцессов. Т.к. каждый процесс выполняется независимо от других, этот метод параллелизма позволяет избежать проблем с GIL. Multiprocessing предоставляет два вида межпроцессного обмена данными: очереди и каналы данных (pipe). Класс Pipe отвечает за канал обмена данными (по умолчанию, двунаправленный), представленный двумя концами, объектами класса Connection. С одним концом канала работает родительский процесс, а с другим концом - подпроцесс.Еще один вид обмена данными может быть достигнут путем записи/чтения обычных файлов. Чтобы исключить одновременную работу двух процессов с одним файлом, в библиотеке есть классы аналогичные threading.