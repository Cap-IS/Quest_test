Для запускуа по расписанию внести данную строку в кронтаб linux: `crontab -e`

где `../scheduler_checker.py` - путь к скрипту

*/15 * * * * /usr/bin/python ../scheduler_checker.py