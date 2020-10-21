# selenium_course__Page_Object

- base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.
- locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать
- main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py
- в test_main_page мы будем хранить сами тест-кейсы, которые будем запускать с помощью pytest, выполняем по префиксу "test_" это для PyTest.
- - Здесь мы будем создавать функции, которым:
- - - выдаём нужный для проверки линк
- - - созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
- - - следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
- - - добавляем проверки, которые создавали методами в main_page.py


# Page_Object

- Page Object содержит в себе методы для работы с веб-страницей
- Page Object - это паттерн для организации кода авто-тестов 

- [ ] Page Object это специальный класс, встроенный в стандартную библиотеку Python
- [x] Паттерн Page Object позволяет хранить селекторы в одном месте, отдельно от логики, что упрощает поддержку автотестов
- [ ] Page Object классы нельзя наследовать друг от друга
- [ ] Методы класса Page Object представляют собой только проверки состояния страницы
- [ ] Без Page Object невозможно писать автотесты
- [x] Page Object уменьшает временные затраты на поддержку автотестов 


#### STEP1
- cd $HOME/selenium_course__Page_Object
- **git clone https://github.com/mirpribili/selenium_course__Page_Object.git**
- cd selenium_course__Page_Object
- git --version
- git status
- git remote set-url origin git@github.com:mirpribili/selenium_course__Page_Object.git
- git remote -v
- git status
- git add .;git commit -m "add readme";git push origin
- **git add .;git commit -m "replace readme";git push origin**

#### STEP2
- pytest -v --tb=line --language=en test_main_page.py

#### STEP3
- **cd $HOME/selenium_course__Page_Object;pytest -v --tb=line --language=en test_main_page.py**
- **conda deactivate; source $HOME/enviroments/selenium_env/bin/activate**

#### STEP4
- **sublime -> View -> indentation -> convert to Tab**
- **pytest -s test_product_page.py**




<span><h2>Немного о Code Style</h2>

<p>Среди тех, кто более или менее регулярно пишет код, существует определенное соглашение о "стиле кода". Стиль кода —&nbsp;это всё то, что не относится к его функциональности: форматирование, имена переменных, функций, констант и так далее. Python прекрасен тем, что&nbsp;его очень легко читать, но даже такой простой для понимания язык в своём коде можно превратить в не читаемую кашу. Не читаемая каша опасна тем, что вы не разберетесь в своем коде уже через пару недель, а другой человек не разберется никогда. Хорошо написанный код экономит время при починке тестов, при внедрении нового человека в команду, да и при написании нового кода тоже. В общем, это очень важная тема, и следует всегда помнить о читабельности кода.</p>

<p>Мы совсем немного затронули эту тему в предыдущих модулях, а теперь, раз уж мы потихоньку идём в сторону большей абстракции, настало время поговорить об этом чуть более подробно.</p>

<h3>&nbsp;Отступы</h3>

<p>Отступы являются частью синтаксиса в Python и означают вложенность блока, будь то тело&nbsp;функции условного выражения, цикла, и так далее. Самое важное для нас в будущих шагах, что все функции внутри класса так же должны быть отделены отступом:</p>

<pre><code class="hljs ruby">@pytest.mark.regression
<span class="hljs-comment"><span class="hljs-comment"># тест вне класса: отступа нет</span></span>
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_student_can_see_lesson_name_in_lesson_in_course_after_joining</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">, driver)</span></span></span></span>:
    <span class="hljs-comment"><span class="hljs-comment"># все строки внутри теста с отступом</span></span>
    page = CoursePromoPage(url=<span class="hljs-keyword"><span class="hljs-keyword">self</span></span>.course.url, driver=driver)
    page.open()


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">TestLessonNameInCourseForTeacher</span></span></span><span class="hljs-class">():</span></span>
    @pytest.mark.regression
    <span class="hljs-comment"><span class="hljs-comment"># тест внутри класса, нужен дополнительный отступ</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_teacher_can_see_lesson_name_in_lesson_in_course</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">, driver)</span></span></span></span>:
        <span class="hljs-comment"><span class="hljs-comment"># еще один отступ для каждой строки, и так с любым уровнем вложенности</span></span>
        page = LessonPlayerPage(url=<span class="hljs-keyword"><span class="hljs-keyword">self</span></span>.lesson_url, driver=driver)
        page.open()
        <span class="hljs-symbol"><span class="hljs-symbol">try:</span></span>
            <span class="hljs-comment"><span class="hljs-comment"># плюс один отступ на каждый уровень вложенности</span></span>
            dangerous_function()
        <span class="hljs-symbol"><span class="hljs-symbol">except:</span></span>
            close_something()

</code></pre>

<p>В некоторых теоретических шагах мы будем давать отдельно функции вне контекста классов, и вам придется расставлять отступы самостоятельно. Будьте готовы и не пугайтесь.</p>

<p>Один отступ — это четыре пробела. Табуляции использовать нежелательно (исключение составляют ситуации, когда&nbsp;вы поддерживаете какой-то уже существующий код с табуляциями, в таком случае смешивать табуляции с пробелами не следует).</p></span>



<span><h2>Code Style: базовые принципы&nbsp;</h2>

<h3>Имена переменных и функций</h3>

<p>Одним из самых важных аспектов читаемого кода является именование: будь то объявление переменных, описание функций, названия классов и так далее. Очень важно, чтобы все имена, которые вы присваивали сущностям, были осмысленными и отражали реальную суть этого объекта. Избегайте&nbsp;однобуквенных и бессмысленных названий типа var1, x, y, my_function, class2 и так далее. Идеальный код — самодокументируемый, к которому не нужны дополнительные пояснения. Если вы чувствуете, что вам хочется написать поясняющий комментарий, это повод переписать код так, чтобы комментарий не понадобился.</p>

<p>Обычно внутри каждой компании есть дополнительные внутренние соглашения о том, как именовать переменные, но общие правила в индустрии&nbsp;примерно одинаковые.</p>

<p>Функции пишутся через_нижнее_подчеркивание:</p>

<p><code>def test_guest_can_see_lesson_name_in_lesson_without_course(self, driver):</code></p>

<p>Классы пишут с помощью CamelCase:</p>

<p><code>class TestLessonNameWithoutCourseForGuest():</code></p>

<p>Константы пишут в стиле UPPERCASE:</p>

<p><code>MAIN_PAGE = "/catalog"</code></p>

<h3>Максимальная простота кода</h3>

<p>Здесь нам на помощь приходят известные принципы написания кода <a href="https://en.wikipedia.org/wiki/Don't_repeat_yourself" rel="noopener noreferrer nofollow" target="_blank">DRY</a> (Don't repeat yourself) и <a href="https://en.wikipedia.org/wiki/KISS_principle" rel="noopener noreferrer nofollow" target="_blank">KISS</a> (Keep it simple, stupid).&nbsp;</p>

<ul>
	<li>Пишите максимально простой код везде, где это возможно.</li>
	<li>Не используйте переусложненных конструкций без большой необходимости (поменьше лямбда-выражений, map&nbsp;и разной другой магии). Если кусок кода можно заменить конструкцией более простой для понимания — замените.</li>
	<li>Пишите максимально линейный код, где это возможно, это проще для восприятия.</li>
	<li>Избегайте большой вложенности блоков кода, такие конструкции тяжело читать.</li>
	<li>Если можно вынести повторяющуюся логику куда-то, выносите, не повторяйтесь.</li>
	<li>По возможности пишите явный код вместо неявного. Чем меньше магии "под капотом", тем лучше.</li>
</ul></span>



<span><h2>Code Style в автотестах</h2>

<p>Здесь мы попытались собрать важные принципы написания автотестов:&nbsp;</p>

<ul>
	<li>Стремитесь к максимальной&nbsp;линейности&nbsp;кода тестов: избегайте ветвления и циклов в тест-кейсах. Если хочется добавить в тесте if, значит, нужно разбить этот тест на два теста или подготовить тестовое окружение так, чтобы не было необходимости использовать ветвление.</li>
	<li>Избегайте зависимых тестов, которые нужно запускать строго в определенном порядке. При росте количества автотестов вы захотите запускать их в несколько потоков параллельно, что будет невозможно при наличии зависимых тестов. А еще зависимые тесты очень не надежны. Подробнее:&nbsp;<a href="http://barancev.github.io/test-deps-are-evil/" rel="noopener noreferrer nofollow" target="_blank">http://barancev.github.io/test-deps-are-evil/</a></li>
	<li>Стремитесь к тому, чтобы тест не полагался на контент, а готовил данные самостоятельно (и удалял после завершения). Используйте чистые браузеры и новых пользователей для лучшей воспроизводимости.</li>
	<li>Абсолютная линейность проверок. Когда вы пишете assert-утверждения в функциях, не следует использовать&nbsp;ветвления и циклы. Логика проверок должна быть линейна, иначе разбор багов и починка автотестов будут стоить очень дорого.</li>
	<li>Именуйте проверки в одинаковом стиле, чтобы по первому взгляду можно было понять, что это именно проверка. Например, можно именовать функции по шаблону should_be_smth:
	<pre><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">should_be_reply_comment</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">()</span></span></span></span></code></pre>
	</li>
	<li>Тесты именуются в одинаковом стиле. Имена тестов должны хорошо отражать различия в похожих сценариях. Можно использовать те же подходы, что и при добавлении имен к тест-кейсам в тестовой документации. Например,&nbsp;<code>test_guest_can_see_teach_button()</code>&nbsp;— обратите внимание на явное указание на роль пользователя.</li>
	<li>Одинаковые тесты, которые отличаются только каким-то контентом (например, языком интерфейса), следует не копировать, а параметризовать.</li>
	<li>Пишите максимально атомарные и неделимые тесты. Не нужно писать один мега-тест, который проверяет вообще всё, напишите лучше десяток маленьких —&nbsp;проще будет локализовать проблему, когда она возникнет.</li>
</ul>

<p>Если у вас нет большого опыта в написании кода, в статьях по ссылкам вы можете&nbsp;найти дополнительные рекомендации по оформлению кода.</p>

<p>Английский язык:</p>

<p><a href="https://docs.python-guide.org/writing/style/" rel="noopener noreferrer nofollow" target="_blank">https://docs.python-guide.org/writing/style/</a></p>

<p><a href="https://www.python.org/dev/peps/pep-0008/" rel="noopener noreferrer nofollow" target="_blank">https://www.python.org/dev/peps/pep-0008/</a></p>

<p>Русский язык:</p>

<p><a href="https://habr.com/ru/post/266969/" rel="noopener noreferrer nofollow" target="_blank">https://habr.com/ru/post/266969/</a></p>

<p><a href="https://habr.com/ru/post/206868/" rel="noopener noreferrer nofollow" target="_blank">https://habr.com/ru/post/206868/</a></p>

<p><a href="https://pep8.ru/doc/pep8/" rel="noopener noreferrer nofollow" target="_blank">https://pep8.ru/doc/pep8/</a></p>

<p><a href="https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html" rel="noopener noreferrer nofollow" target="_blank">https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html</a></p></span>


<span><h2>Подготовка окружения</h2>

<p>В этом модуле мы создадим с нуля полноценный тестовый проект, который будет являться вашим финальным заданием. Для этого будем использовать популярные в индустрии инструменты&nbsp;Git и GitHub,&nbsp;с которыми в общих чертах мы познакомились в предыдущем модуле.&nbsp;</p>

<p>Добавлять изменения мы будем постепенно, чтобы в вашем репозитории была красивая история коммитов. Потому что именно так происходит написание промышленного кода, а наша задача в этом курсе — максимально приблизиться к этому процессу.&nbsp;</p>

<p>Итак:</p>

<ol>
	<li>Создайте отдельный <strong>публичный</strong> репозиторий с осмысленным названием на GitHub.</li>
	<li>Склонируйте его к себе на локальную машину.</li>
	<li>Добавьте туда файл <em>conftest.py&nbsp;</em>из предыдущего модуля. Убедитесь дополнительно, что там есть параметр для задания языка интерфейса, по умолчанию равный&nbsp;"<strong>en</strong>".</li>
	<li>Убедитесь что ни во вложенных папках, ни во внешних папках нет других файлов <em>conftest.py</em>, почему это важно смотри здесь:&nbsp;<a href="https://stepik.org/lesson/237240/step/4" rel="noopener noreferrer nofollow">Conftest.py — конфигурация тестов</a>.</li>
	<li>Добавьте в репозиторий&nbsp;файл <em>requirements.txt&nbsp;</em>из предыдущего модуля.&nbsp;</li>
	<li>Создайте пустой файл <em>__init__.py</em>,&nbsp;чтобы работали относительные импорты.</li>
	<li>Создайте файл<em> </em><em>test_main_page.py&nbsp;</em>и добавьте в него тест из предыдущего модуля:&nbsp;
	<pre><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_can_go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser)</span></span></span></span>:
    link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>
    browser.get(link)
    login_link = browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
    login_link.click()</code></pre>
	</li>
	<li>Не забудьте активировать окружение, которое мы создали ранее. Опционально, можно создать для этого проекта новое виртуальное окружение&nbsp;для удобства.&nbsp;В&nbsp;таком случае убедитесь что вы установили туда все необходимые пакеты из <em>requirements.txt.&nbsp;</em>А еще не стоит добавлять файлы окружения в репозиторий и вообще в отслеживаемые&nbsp;—&nbsp;лишние&nbsp;файлы на GitHub&nbsp;это моветон.&nbsp;</li>
	<li>Убедитесь, что тест работает, с помощью следующей команды:&nbsp;<code>pytest -v --tb=line --language=en test_main_page.py</code>. Здесь и далее мы будем использовать эту команду для запуска.&nbsp;В этой команде мы использовали опцию PyTest <strong>--tb=line</strong>, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста. Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.&nbsp;</li>
	<li>Добавьте все новые файлы в Git командой <code><strong>git add *</strong></code></li>
	<li>Проверьте, что нужные файлы попали в планируемый коммит:&nbsp;<code><strong>git status</strong></code></li>
	<li>Зафиксируйте изменения коммитом с осмысленным сообщением: <code><strong>git commit -m "write your message".</strong></code></li>
	<li>По желанию&nbsp;добавьте описание репозитория с описанием вашего тестового проекта.</li>
</ol></span>


<span><h2>Что такое Page Object Model?</h2>

<p><strong>Page Object Model</strong> или кратко Page Object&nbsp;— это паттерн программирования, который очень популярен в автоматизации тестирования&nbsp;и является одним из стандартов при автоматизации тестирования веб-продуктов. Это также один из удобных способов структурировать свой код таким образом, чтобы его было удобно поддерживать, менять и работать с ним.</p>

<p>Основная идея состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса. Способы взаимодействия пользователя со страницей можно описать с помощью методов класса. В идеале тест, который будет использовать Page Object, должен&nbsp;описывать бизнес-логику тестового сценария&nbsp;и скрывать Selenium-методы взаимодействия с браузером и страницей. При изменениях в верстке страницы не придется исправлять&nbsp;тесты, связанные с этой страницей. Вместо этого нужно будет поправить только класс, описывающий страницу.</p>

<p>То есть&nbsp;здесь применяются те же принципы, что и в разработке: мы хотим повысить читаемость кода&nbsp;и вынести в абстрактные методы все детали. Тесты должны быть просто и понятно написаны, а повторяющиеся куски кода выделены в отдельные функции. В Page Object мы отделяем логику действий, например, авторизовать пользователя, от конкретной реализации (найти поле почты, ввести туда данные, найти поле пароля, ввести туда данные, найти кнопку и т.д.).&nbsp;</p>

<p>Рассмотрим такой простой тест-кейс:</p>

<ol>
	<li>Открыть главную страницу</li>
	<li>Перейти на страницу логина</li>
</ol>

<p>Ожидаемый результат:</p>

<p>Открыта страница логина</p>

<p>&nbsp;</p>

<p>Давайте посмотрим на кусочек кода теста из предыдущего модуля, который реализует первую часть этого теста:</p>

<p><em>test_main_page.py:</em></p>

<pre><code class="language-python hljs">link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>


<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_can_go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser)</span></span></span><span class="hljs-function">:</span></span>
    browser.get(link)
    login_link = browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
    login_link.click()
</code></pre>

<p>Что здесь происходит?</p>

<p>Мы открываем ссылку, находим элемент с определенным селектором и нажимаем на этот элемент.</p>

<p>Что мы на самом деле имеем в виду?</p>

<p>Мы хотим открыть страницу логина. Давайте выделим это действие в отдельную функцию с понятным названием, пока все в том же файле <em>test_main_page</em>.py :</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser)</span></span></span><span class="hljs-function">:</span></span>
    login_link = browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
    login_link.click()</code></pre>

<p>и наш тест упрощается:</p>

<pre><code class="hljs armasm"><span class="hljs-symbol"><span class="hljs-symbol">def</span></span> test_guest_can_go_to_login_page(<span class="hljs-keyword"><span class="hljs-keyword">browser): </span></span>
   <span class="hljs-keyword"><span class="hljs-keyword">browser.get(link) </span></span>
   go_to_login_page(<span class="hljs-keyword"><span class="hljs-keyword">browser) </span></span></code></pre>

<p>При написании следующих тестов, когда нам понадобится перейти к странице логина с главной страницы, нам не нужно будет копировать этот кусочек кода или писать заново —&nbsp;мы сможем переиспользовать уже написанный метод.</p>

<p>Круто? А мы еще даже не написали Page Object. Дальше будет круче.</p>

<p>Дополнительно про Page Object вы можете почитать здесь:</p>

<p><a href="https://github.com/SeleniumHQ/selenium/wiki/PageObjects" rel="noopener noreferrer nofollow" target="_blank">https://github.com/SeleniumHQ/selenium/wiki/PageObjects</a></p>

<p><a href="https://martinfowler.com/bliki/PageObject.html" rel="noopener noreferrer nofollow" target="_blank">https://martinfowler.com/bliki/PageObject.html</a></p>

<p><a href="https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b" rel="nofollow noopener noreferrer" target="_blank">https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b</a></p></span>


<span><h2>Почему именно Page Object?</h2>

<p>Можно, конечно, хранить всю логику наших тестов в одном файле под каким-нибудь условным названием steps.py, и для начала это уже неплохо. Но если мы тестируем большой веб-продукт с множеством разных состояний и переходов, этот файл может разрастись до огромных размеров, и найти в нем нужный метод будет непросто. Еще бывают ситуации, когда на разных страницах логически один и тот же метод имеет разную реализацию.&nbsp;Например, у нашего интернет-магазина может быть метод "добавить в корзину". Но пользователь может добавлять товар в корзину&nbsp;как со страницы каталога, так и со страницы самого товара.&nbsp;</p>

<p>Было бы удобно выделить все методы, которые логически относятся к одной веб-странице в нашем продукте, в отдельный класс в нашем коде. Отсюда и название Page Object&nbsp;— это абстрактный объект, который содержит в себе методы для работы с конкретной веб-страницей.&nbsp;</p>

<p><strong>Важно! </strong>Обычно методы у Page Object&nbsp;бывают двух типов: <em>сделать что-то</em> и <em>проверить что-то.</em></p>

<p>Рассмотрим страницу товара в интернет магазине <a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/</a>.</p>

<p>Какие могут быть методы у Page Object, ассоциированного с такой страницей? Запишем основные сценарии:&nbsp;</p>

<ul>
	<li>добавить в корзину;</li>
	<li>проверить,&nbsp;что есть сообщение об успешном добавлении в корзину;</li>
	<li>перейти к написанию отзыва;</li>
	<li>проверить,&nbsp;что есть название, цена, описание товара;</li>
	<li>вернуться на главную.</li>
</ul>

<p>Обратите внимание, что все проверки у нас тоже становятся отдельными&nbsp;методами. В самом тест-кейсе не остается никаких вспомогательных слов типа assert, только описание шагов. Прямо как в нашей тестовой документации.&nbsp;&nbsp;</p>

<p>Тесты будут выглядеть примерно так:</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_add_to_cart</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser)</span></span></span><span class="hljs-function">:</span></span>
    page = ProductPage(url=<span class="hljs-string"><span class="hljs-string">""</span></span>, browser)   <span class="hljs-comment"><span class="hljs-comment"># инициализируем объект Page Object</span></span>
    page.open()                           <span class="hljs-comment"><span class="hljs-comment"># открываем страницу в браузере</span></span>
    page.should_be_add_to_cart_button()   <span class="hljs-comment"><span class="hljs-comment"># проверяем что есть кнопка добавления в корзину</span></span>
    page.add_product_to_cart()            <span class="hljs-comment"><span class="hljs-comment"># жмем кнопку добавить в корзину </span></span>
    page.should_be_success_message()      <span class="hljs-comment"><span class="hljs-comment"># проверяем что есть сообщение с нужным текстом</span></span>
</code></pre></span>


 Сама идея описывать взаимодействие с продуктом со стороны пользователя выглядит интересно. Но вот реализация ScreenPlay выглядит тяжеловато - смотрю на нее, и не хочется с PageObject на нее переходить.

Кажется, что ScreenPlay больше подходит для заказной разработки, когда есть заказчик, которому нужна прозрачность в том, на что тратит время отдел тестирования. Это также видно в том, что примеры ScreenPlay часто приводят вместе с BDD подходом, который также близок аутсорсинговым компаниям. Для продуктовой компании PageObject выглядит все-таки понятнее, проще, т.к. тестирование обычно это внутренний процесс в компании.

<span><h2>Базовая страница для проекта: BasePage</h2>

<p>Давайте перепишем тест из файла&nbsp;<em>test_main_page.py</em>&nbsp;с помощью паттерна&nbsp;Page Object, который мы добавили на этапе <a href="https://stepik.org/lesson/199980/step/6?unit=174035" rel="noopener noreferrer nofollow">подготовки окружения.</a>&nbsp;Мы будем работать&nbsp;с главной страницей нашего приложения, поэтому дадим&nbsp;классу говорящее название&nbsp;MainPage.&nbsp;</p>

<p><strong>Важно! </strong>В этом уроке мы напишем самостоятельно простую реализацию паттерна Page Object. А в следующих уроках уже рассмотрим существующие фреймворки и то, как они могут облегчить нам жизнь. Сейчас самая главная задача — осознать принципы работы.&nbsp;</p>

<p>1. Создайте в своем проекте папку pages, там мы будем хранить все наши Page Object&nbsp;</p>

<p>2. В папке создайте два файла: <code>base_page.py</code> и <code>main_page.py </code>&nbsp;</p>

<p>Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем&nbsp;вспомогательные методы для работы с драйвером.</p>

<p>3. В файле <code>base_page.py</code> создайте класс с названием <code>BasePage</code>.&nbsp;</p>

<p>В Python такие вещи делаются с помощью следующей конструкции:&nbsp;</p>

<pre><code class="hljs python"><span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">BasePage</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span></code></pre>

<p>4. Теперь в наш класс нужно добавить методы. Первым делом добавим <em>конструктор —&nbsp;</em>метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом <code>__init__</code>. В него в качестве параметров мы передаем экземпляр драйвера и url адрес. Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. Получается примерно так:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">__init__</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, browser, url)</span></span></span><span class="hljs-function">:</span></span>
    self.browser = browser
    self.url = url</code></pre>

<p>5. Теперь добавим еще один&nbsp;метод open. Он должен открывать нужную страницу в браузере, используя метод get().</p>

<p>Объявите ниже в том же классе:</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">open</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span></code></pre>

<p>и реализуйте этот метод: нужна всего одна строка. Эту строку нужно отправить в качестве ответа на&nbsp;это задание, без отступов.&nbsp;</p>

<p>6. После того как Stepik принял ваш ответ как правильный, добавьте новые файлы в Git и зафиксируйте изменения коммитом (не забудьте осмысленное сообщение).</p>

<p>&nbsp;</p>

<p>В итоге у вас должен следующий код в файле&nbsp;<em>base_page.py</em>:&nbsp;</p>

<pre><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">BasePage</span></span></span><span class="hljs-class">():</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">__init__</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">, browser, url)</span></span></span></span>:
        <span class="hljs-keyword"><span class="hljs-keyword">self</span></span>.browser = browser
        <span class="hljs-keyword"><span class="hljs-keyword">self</span></span>.url = url

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">open</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">)</span></span></span></span>: 
        <span class="hljs-comment"><span class="hljs-comment"># ваша реализация</span></span></code></pre></span>


<span><h2>Page Object для главной страницы сайта</h2>

<p>Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина.&nbsp;</p>

<p>1. Откройте файл <code>main_page.py</code>&nbsp;</p>

<p>2. В нем нужно сделать импорт базового класса BasePage:&nbsp;</p>

<pre><code class="hljs armasm"><span class="hljs-symbol"><span class="hljs-symbol">from</span></span> .<span class="hljs-keyword"><span class="hljs-keyword">base_page </span></span><span class="hljs-meta"><span class="hljs-meta">import</span></span> <span class="hljs-keyword"><span class="hljs-keyword">BasePage</span></span></code></pre>

<p>3. В нем создайте класс&nbsp; <code>MainPage</code>. Его нужно сделать наследником класса <code>BasePage</code>. Класс-предок в Python указывается в скобках:&nbsp;</p>

<pre><code class="hljs haskell"><span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-type"><span class="hljs-class"><span class="hljs-type">MainPage</span></span></span><span class="hljs-class">(</span><span class="hljs-type"><span class="hljs-class"><span class="hljs-type">BasePage</span></span></span><span class="hljs-class">): </span></span></code></pre>

<p>таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.&nbsp;</p>

<p>4. Перенесите&nbsp;метод из предыдущего урока в класс <code>MainPage</code>:</p>

<pre><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser)</span></span></span></span>:
&nbsp; &nbsp;login_link = browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
   login_link.click()&nbsp;</code></pre>

<p>Чтобы все работало, надо слегка видоизменить&nbsp;его. В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент <code>self</code>&nbsp;, чтобы иметь доступ к атрибутам и методам класса:&nbsp;</p>

<p><code>def go_to_login_page(self):</code></p>

<p>Так как браузер у нас хранится&nbsp;как аргумент класса <code>BasePage</code>, обращаться к нему нужно соответствующим образом&nbsp;с помощью <code>self</code>:&nbsp;</p>

<pre><code class="language-python hljs">self.browser.find_element_by_css_selector(<span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)</code></pre>

<p>Заодно заменим find на более универсальный:&nbsp;</p>

<pre><code class="hljs stylus">self<span class="hljs-selector-class"><span class="hljs-selector-class">.browser</span></span><span class="hljs-selector-class"><span class="hljs-selector-class">.find_element</span></span>(By<span class="hljs-selector-class"><span class="hljs-selector-class">.CSS_SELECTOR</span></span>, <span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)</code></pre>

<p>Итого, файл <em>main_page.py:&nbsp;</em></p>

<pre><code class="hljs python"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> .base_page <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> BasePage
<span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium.webdriver.common.by <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> By

<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">MainPage</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">(BasePage)</span></span></span><span class="hljs-class">:</span></span> 
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        login_link = self.browser.find_element(By.CSS_SELECTOR, <span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
        login_link.click()</code></pre></span>


<span><h2>Первый тест на основе&nbsp;Page Object</h2>

<p>Ура, первый прототип страницы мы уже реализовали! Давайте теперь перепишем тест с помощью Page Object:&nbsp;</p>

<p>1. Откройте файл с вашим тестом&nbsp;<em>test_main_page.py</em></p>

<p>2. В самом верху файла нужно импортировать класс, описывающий главную страницу:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> .pages.main_page <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> MainPage</code></pre>

<p>3. Теперь преобразуем сам тест в <em>test_main_page.py</em>:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> .pages.main_page <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> MainPage


<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_can_go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser)</span></span></span><span class="hljs-function">:</span></span>
    link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span>
    page = MainPage(browser, link)   <span class="hljs-comment"><span class="hljs-comment"># инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес </span></span>
    page.open()                      <span class="hljs-comment"><span class="hljs-comment"># открываем страницу</span></span>
    page.go_to_login_page()          <span class="hljs-comment"><span class="hljs-comment"># выполняем метод страницы — переходим на страницу логина</span></span></code></pre>

<p>4. Убедитесь, что тест проходит, запустив его все той же командой:&nbsp;</p>

<pre><code class="hljs routeros">pytest -v <span class="hljs-attribute"><span class="hljs-attribute">--tb</span></span>=line <span class="hljs-attribute"><span class="hljs-attribute">--language</span></span>=en test_main_page.py
</code></pre>

<p>5.&nbsp;Добавьте изменения и сделайте коммит (с осмысленным сообщением!)</p>

<p>Теперь наш тест <strong>почти </strong>полностью написан в модном стиле Page Object! Почему <strong>почти&nbsp;</strong>— узнаете в следующих шагах.</p>

<p>Обратите внимание на&nbsp; структуру файлов на данном этапе:&nbsp;</p>

<p><img alt="" src="https://ucarecdn.com/b72c7bb8-0ed0-40af-8ad0-b444197247d7/"></p></span>

<span><h2>Элементы страниц в паттерне Page Object</h2>

<p>Помните, мы говорили о том, что тесты почти соответствуют подходу&nbsp;Page Object?&nbsp;</p>

<p>Сейчас разберемся, почему <strong>почти&nbsp;</strong>на примере короткой и поучительной истории.</p>

<p>У нас уже есть два тест-кейса, которые так или иначе взаимодействуют со ссылкой на логин. Представим себе&nbsp;ситуацию, что у нас модный быстрый&nbsp;agile: разработчики постоянно вносят изменения в продукт. В&nbsp;какой-то прекрасный момент изменения коснулись и шапки сайта. Вот приходит к вам разработчик с новой ссылкой и говорит протестировать.</p>

<p>Замените линк, на котором запускаются тесты на <a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer</a>&nbsp;</p>

<p>Запустите тесты командой:</p>

<pre><code class="language-bash hljs">pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>Тесты упали, и теперь нам нужно их поддерживать, то есть <em>чинить.&nbsp;</em>Подберите новый селектор к ссылке на логин.&nbsp;</p>

<p>Нам придется&nbsp;поправить в файле <em>main_page.py</em>&nbsp;несколько мест, где используется измененный селектор. Посчитайте, сколько строк вам нужно будет отредактировать, чтобы починить ваши тесты, и внесите полученное число&nbsp;в первое поле ответа ниже.&nbsp;</p>

<p>Чтобы этого избежать, при проектировании тестов (да и вообще кода) хорошей практикой является выносить селектор&nbsp;во внешнюю переменную.&nbsp;</p>

<p>Давайте этим и займемся:&nbsp;</p>

<p>1. В папке pages создайте новый файл <em>locators.py&nbsp;</em></p>

<p>2. Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject:&nbsp;</p>

<pre><code class="hljs stylus">from selenium<span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class">.webdriver</span></span></span></span><span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class">.common</span></span></span></span><span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class">.by</span></span></span></span> import By


class MainPageLocators():
    LOGIN_LINK = (By<span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class"><span class="hljs-selector-class">.CSS_SELECTOR</span></span></span></span>, <span class="hljs-string"><span class="hljs-string"><span class="hljs-string"><span class="hljs-string">"#login_link"</span></span></span></span>)</code></pre>

<p>теперь каждый селектор&nbsp;— это пара: как искать и что искать.&nbsp;</p>

<p>3. В файле main_page.py импортируйте новый класс с локаторами&nbsp;</p>

<pre><code class="hljs capnproto"><span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span></span></span> .locators <span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span></span></span> MainPageLocators</code></pre>

<p>4. Теперь в классе MainPage замените все&nbsp;строки, где содержится "<strong>#login_link</strong>" таким образом:</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span></span></span></span></span><span class="hljs-function"><span class="hljs-function"><span class="hljs-function"> </span></span></span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title"><span class="hljs-function"><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">should_be_login_link</span></span></span></span></span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params"><span class="hljs-function"><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span></span></span></span></span><span class="hljs-function"><span class="hljs-function"><span class="hljs-function">:</span></span></span></span>
    <span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword">assert</span></span></span></span> self.is_element_present(*MainPageLocators.LOGIN_LINK), <span class="hljs-string"><span class="hljs-string"><span class="hljs-string"><span class="hljs-string">"Login link is not presented"</span></span></span></span></code></pre>

<p>Обратите внимание здесь на символ<strong> *</strong>, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.&nbsp;</p>

<p>5. Запустите тесты с помощью той же самой команды:&nbsp;</p>

<pre><code class="language-bash hljs">pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>Они,&nbsp;конечно, снова упадут. Но теперь посчитайте, сколько строк вам нужно будет отредактировать, когда тесты написаны в такой конфигурации? Внесите число во второе поле ответа.&nbsp;</p>

<p>&nbsp;</p>

<p><strong>Итак, PageObject&nbsp;— это не только <em>методы</em>, но и <em>элементы</em>.&nbsp;&nbsp;</strong></p>

<p>Исправлять руками сломанные селекторы во всем проекте&nbsp;— долго и муторно, и есть большой риск забыть и оставить старый селектор. Когда мы выносим селекторы в отдельную сущность, мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе.&nbsp;</p>

<p>А ещё&nbsp;спринт спустя промоакция закончилась, и фичу с изменением шапки откатили назад.&nbsp;Теперь ссылка&nbsp;работает так же, как раньше. Удалите ссылку с промоакцией, и верните обычную ссылку для запуска тестов:&nbsp;</p>

<pre><code class="hljs ini"><span class="hljs-attr"><span class="hljs-attr"><span class="hljs-attr"><span class="hljs-attr">link</span></span></span></span> = <span class="hljs-string"><span class="hljs-string"><span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/"</span></span></span></span></code></pre>

<p>Не забудьте вернуть старый&nbsp;селектор <strong>#login_link</strong>, так чтобы тесты снова проходили. Они&nbsp;нам еще пригодятся!&nbsp;</p></span>


<span><h2>Реализация LoginPage</h2>

<p>Если вы хорошо ориентируетесь в тест-дизайне, скорее всего вас немного коробит тест с переходом к логину&nbsp;— там ведь нет никаких проверок.&nbsp;Давайте&nbsp;проверим,&nbsp;что мы действительно перешли на страницу логина. Для этого нам&nbsp;будет нужен&nbsp;новый Page Object. Заодно разберемся, как между ними переключаться в ходе теста.&nbsp;</p>

<p>Скачайте <a href="https://stepik.org/media/attachments/lesson/199980/login_page.py" rel="noopener noreferrer nofollow">файл</a> с шаблоном&nbsp;для LoginPage. Добавьте его в папку pages. Внутри есть заглушки для методов проверок:&nbsp;</p>

<pre><code class="hljs mipsasm"><span class="hljs-keyword"><span class="hljs-keyword">should_be_login_url
</span></span><span class="hljs-keyword"><span class="hljs-keyword">should_be_login_form
</span></span><span class="hljs-keyword"><span class="hljs-keyword">should_be_register_form</span></span></code></pre>

<p>Реализуйте их самостоятельно:&nbsp;</p>

<p>1. В файле locators.py создайте класс&nbsp;LoginPageLocators&nbsp;</p>

<p>2. Подберите селекторы к формам регистрации и логина, добавьте их в класс&nbsp;LoginPageLocators</p>

<p>3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке. Напишите сначала красный тест, чтобы убедиться в понятности вывода.&nbsp;</p>

<p>4. В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url&nbsp;браузера. Для этого используйте соответствующее&nbsp;<a href="https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url" rel="noopener noreferrer nofollow" target="_blank">свойство Webdriver</a>.</p>

<p>5. Добавьте изменения в коммит с осмысленным сообщением</p>

<p>Теперь посмотрим,&nbsp;как можно осуществлять переход между страницами.&nbsp;</p></span>




<span><h2>Переходы между страницами</h2>

<p>Переход можно реализовать двумя разными способами.&nbsp;</p>

<p>Первый способ: возвращать нужный Page Object.</p>

<p>Для этого в файле main_page.py нужно сделать импорт страницы с логином:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> .login_page <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> LoginPage</code></pre>

<p>Затем в методе, который осуществляет переход к&nbsp;странице логина, проинициализировать новый объект Page&nbsp;и вернуть его:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> LoginPage(browser=self.browser, url=self.browser.current_url) </code></pre>

<p>Обратите внимание! При создании объекта мы обязательно&nbsp;передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.</p>

<p>Теперь в тесте нам не нужно думать про инициализацию страницы: она уже создана. Сохранив возвращаемое значение в переменную, мы можем использовать методы новой страницы в тесте:</p>

<pre><code class="hljs routeros">def test_guest_can_go_to_login_page(browser):
    link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com"</span></span>
   <span class="hljs-built_in"><span class="hljs-built_in"> page </span></span>= MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()</code></pre>

<p>Плюсы такого подхода:&nbsp;</p>

<ul>
	<li>тест выглядит аккуратнее — не нужно инициализировать страницу в теле теста;</li>
	<li>явно возвращаем страницу — тип страницы ассоциирован с методом;</li>
	<li>не нужно каждый раз думать в разных тестах про инициализацию страницы — уменьшаем дублирование кода;</li>
</ul>

<p>минусы:&nbsp;</p>

<ul>
	<li>если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов;</li>
	<li>большая связность кода — при изменении логики придется менять возвращаемое значение;</li>
	<li>сложнее понимать код, так как&nbsp;страница инициализируется неявно;</li>
	<li>образуются циклические зависимости, что часто приводит к ошибкам.</li>
</ul>

<p>Второй подход: переход происходит неявно, страницу инициализируем в теле теста:&nbsp;</p>

<p>1. Закомментируйте строку с возвращаемым значением&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    <span class="hljs-comment"><span class="hljs-comment"># return LoginPage(browser=self.browser, url=self.browser.current_url) </span></span></code></pre>

<p>2. Инициализируем LoginPage в теле теста (не забудьте импортировать в файл нужный класс):&nbsp;</p>

<pre><code class="hljs routeros"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com"</span></span>
   <span class="hljs-built_in"><span class="hljs-built_in"> page </span></span>= MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()</code></pre>

<p>Плюсы:</p>

<ul>
	<li>меньше связность кода;</li>
	<li>меньше импортов, нет перекрестных импортов;</li>
	<li>больше гибкость;</li>
	<li>в тесте понятнее что происходит, т.к. явно инициализируем страницу.</li>
</ul>

<p>Минусы:</p>

<ul>
	<li>появляется лишний шаг в тест-кейсе;</li>
	<li>каждый раз при написании теста нужно думать про корректные переходы;</li>
	<li>дублируется код.</li>
</ul>

<p>И тот и другой подход можно успешно применять в своих проектах, главное делать это с умом. Сейчас оставьте второй вариант с явной инициализацией страниц в теле теста, чтобы избежать лишних сложностей с циклическими зависимостями.&nbsp;</p>

<p>Уберите лишний закомментированный код, и зафиксируйте изменения в коммите с осмысленным сообщением.</p></span>


<span><h2>Задание: добавление в корзину со страницы товара</h2>

<p>Давайте,&nbsp;прежде чем двигаться дальше, закрепим знания на практике.&nbsp;</p>

<p>Представьте, что вы работаете тестировщиком-автоматизатором в IT-отделе интернет-магазина. QA Lead&nbsp;поручил вам&nbsp;задание автоматизировать следующий тестовый сценарий:&nbsp;</p>

<ol>
	<li>Открываем страницу товара (<a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear</a>). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.</li>
	<li>Нажимаем на кнопку "Добавить в корзину".</li>
	<li>*Посчитать результат математического выражения и ввести ответ. Используйте для этого метод <strong>solve_quiz_and_get_code()</strong>, который приведен ниже. Например, можете добавить его в класс <strong>BasePage</strong>, чтобы использовать его на любой странице. Этот метод&nbsp;нужен только для проверки того, что вы написали тест на Selenium.&nbsp;После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.</li>
</ol>

<p>Ожидаемый результат:&nbsp;</p>

<ol>
	<li>Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.</li>
	<li>Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.&nbsp;</li>
</ol>

<p>Тест нужно написать, используя паттерн&nbsp;Page Object. Для этого вам нужно:&nbsp;</p>

<ol>
	<li>Добавить новый файл для тест-кейсов, связанных со страницей товара<em>.&nbsp;</em>Назовите файл с тестами<em> test_product_page.py.</em></li>
	<li>Создать класс Page Object для страницы товара. Опишите его в файле <em>product_page.py</em> в папке <em>pages.</em></li>
	<li>Описать в нем метод для добавления в корзину.</li>
	<li>Дописать&nbsp;методы-проверки.</li>
	<li>Описать необходимые локаторы к элементам страницы.</li>
	<li>Написать сам тест-кейс, используя все вышеописанное. Назовите тест <strong>test_guest_can_add_product_to_basket.</strong></li>
</ol>

<p>Можете начинать работу с любого пункта, но хорошей практикой считается написать сначала шаги и структуру теста, а потом описывать конкретную реализацию.&nbsp;</p>

<p>*Используйте этот метод в тесте для получения проверочного кода:&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> selenium.common.exceptions <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> NoAlertPresentException <span class="hljs-comment"><span class="hljs-comment"># в начале файла</span></span>

<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">solve_quiz_and_get_code</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
    alert = self.browser.switch_to.alert
    x = alert.text.split(<span class="hljs-string"><span class="hljs-string">" "</span></span>)[<span class="hljs-number"><span class="hljs-number">2</span></span>]
    answer = str(math.log(abs((<span class="hljs-number"><span class="hljs-number">12</span></span> * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    <span class="hljs-keyword"><span class="hljs-keyword">try</span></span>:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(<span class="hljs-string"><span class="hljs-string">f"Your code: </span><span class="hljs-subst"><span class="hljs-string"><span class="hljs-subst">{alert_text}</span></span></span><span class="hljs-string">"</span></span>)
        alert.accept()
    <span class="hljs-keyword"><span class="hljs-keyword">except</span></span> NoAlertPresentException:
        print(<span class="hljs-string"><span class="hljs-string">"No second alert presented"</span></span>)</code></pre>

<p>Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром <strong>-s</strong>:</p>

<pre><code class="hljs css"><span class="hljs-selector-tag"><span class="hljs-selector-tag">pytest</span></span> <span class="hljs-selector-tag"><span class="hljs-selector-tag">-s</span></span> <span class="hljs-selector-tag"><span class="hljs-selector-tag">test_foo</span></span><span class="hljs-selector-class"><span class="hljs-selector-class">.py</span></span></code></pre></span>



<span><h2>Задание: независимость от данных</h2>

<p>Хорошие автотесты должны быть максимально&nbsp;независимы от данных. Худшее, что можно сделать в тесте это "захардкодить"&nbsp;проверки для объектов, которые существуют только на вашем конкретном инстансе. Почему? Потому что данные будут постоянно меняться, и при каждом таком изменении придется чинить автотесты. Еще это ухудшает переиспользование метода: допустим,&nbsp;мы хотим прогнать тест для множества товаров, тогда придется писать большое количество проверок: по одной для каждого товара. В конечном итоге, это сказывается на качестве продукта,&nbsp;так как такие&nbsp;тесты работают на узкой выборке страниц.</p>

<p>Общая рекомендация: ваши тесты не должны зависеть от того, что вы&nbsp;не можете контролировать. Это может быть информация, уже хранящаяся в базе данных,&nbsp;или сторонние сервисы, которые использует ваше приложение. Вы можете проверять конкретные данные только в случае, когда используете специально подготовленную&nbsp;тестовую базу, инициируемую перед каждым запуском тестов,&nbsp;или добавляете нужные&nbsp;данные в базу данных напрямую&nbsp;или через API приложения.&nbsp;</p>

<p>Попробуйте запустить автотест, который мы написали на предыдущем шаге, на странице&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" rel="noopener noreferrer nofollow" style="font-size: inherit; font-weight: inherit;" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019</a>.</p>

<p>Если&nbsp;в предыдущем тесте после добавления товара в корзину вы&nbsp;проверяли в сообщении сайта фиксированную строку "The shellcoder's handbook",&nbsp;то тест упадет, так как теперь мы добавили другой товар. Если тест прошел, то вы молодец и можете просто вставить новый проверочный код в этом задании.&nbsp;</p>

<p>Чтобы тест был независимым от контента:&nbsp;</p>

<ul>
	<li>Измените методы проверки таким образом, чтобы они принимали как аргумент название товара и цену товара.</li>
	<li>Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.</li>
	<li>Сделайте такой же метод для цены.</li>
	<li>Теперь проверяйте, что название товара в сообщении совпадает с заголовком товара.</li>
</ul></span>



<span><h2>Задание: независимость контента, ищем баг</h2>

<p>Эта задача для настоящих ниндзя автотестинга. Не потому что она сложная, а потому что сейчас мы будем ловить с вами настоящий баг с помощью наших автотестов.&nbsp;Для нашего интернет-магазина было запущено несколько новых промо-акций, одна из которых привела к появлению&nbsp;бага. Промо-акция включается путем добавления параметра ?promo=offerN к ссылке на товар.</p>

<p>К счастью, нам не придется менять наш тест, чтобы проверить изменения в коде. Мы просто&nbsp;запустим&nbsp;всё тот же тест на странице&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/</a>&nbsp;с параметризацией. Вам нужно определить,&nbsp;при каком значении параметра promo автотест&nbsp;упадет. Для этого проверьте результат работы PyTest и найдите url, на котором произошла ошибка. Значение параметра может изменяться от offer0 до offer9.</p>

<p>Пример ссылки:&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0</a>. Если баг будет найден на этой странице, то введите в качестве ответа <a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0</a>.</p>

<p>Запустить сразу несколько тестов вы можете, используя <strong>@pytest.mark.parametrize</strong>. Мы уже сделали для вас шаблон теста:</p>

<pre><code class="hljs ruby">@pytest.mark.parametrize(<span class="hljs-string"><span class="hljs-string">'link'</span></span>, [<span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"</span></span>,
                                  <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"</span></span>])
<span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">test_guest_can_add_product_to_basket</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(browser, link)</span></span></span></span>:
    <span class="hljs-comment"><span class="hljs-comment"># ваша реализация теста</span></span></code></pre>

<p>Подсказка: баг должен быть найден методом проверки.</p>

<p>После того как вы обнаружили баг, учитывая что чинить его не собираются, лучше всего пометить падающий тест как <strong>xfail</strong>&nbsp;или <strong>skip.&nbsp;</strong>Помните, как мы такое проворачивали в третьем модуле?&nbsp;Освежить память: <a href="/lesson/236918/step/5?unit=209305" rel="noopener noreferrer nofollow">XFail: помечать тест как ожидаемо падающий</a>.</p>

<p>С параметризацией делается это примерно так:&nbsp;&nbsp;</p>

<pre><code class="language-python hljs"><span class="hljs-meta"><span class="hljs-meta">@pytest.mark.parametrize('link', ["okay_link",</span></span>
                                  pytest.param(<span class="hljs-string"><span class="hljs-string">"bugged_link"</span></span>, marks=pytest.mark.xfail),
                                  <span class="hljs-string"><span class="hljs-string">"okay_link"</span></span>])</code></pre>

<p>Подробнее:&nbsp;<a href="https://docs.pytest.org/en/latest/skipping.html#skip-xfail-with-parametrize" rel="noopener noreferrer nofollow" target="_blank">Skip/xfail with parametrize</a></p>

<p>После всех манипуляций не забудьте зафиксировать изменения коммитом.</p></span>


<span><h2>Отрицательные проверки: как проверить отсутствие элемента</h2>

<p>Иногда в ходе написания авто-тестов возникает ситуация, когда нам нужно проверить не только присутствие элемента на странице, но и то, что элемента на странице нет. Здесь стоит разделять две принципиально разные ситуации, в зависимости от того как ведет себя веб-приложение:&nbsp;</p>

<p>&nbsp;<strong>1. Элемент потенциально может появится на странице</strong> (но вообще-то не должен). Например, мы&nbsp;открываем страницу товара, и ожидаем, что там нет сообщения об успешном добавлении в корзину. Мы проверяем, что элемента нет, но при позитивном сценарии, когда мы добавляем товар в корзину, сообщение тоже появляется не сразу. Если при негативной проверке мы не добавим ожидание, а сразу выдадим результат: <span style="color: #66cc66;">"True, элемента действительно нет, все хорошо"</span>, мы рискуем нарваться на ложно-зеленый тест. То есть, можем пропустить баг.&nbsp;</p>

<p><strong>2. Элемент присутствует на странице и должен исчезнуть</strong> со временем или в результате действий пользователя. Это может быть, например, удаление товара из корзины, или исчезновение лоадера с загрузкой.&nbsp;</p>

<h3>Почему нужно писать такие проверки с осторожностью?&nbsp;</h3>

<p><em>Во-первых</em>, нам приходится всегда гарантированно ждать. В первом примере&nbsp;нам всегда нужно ждать несколько секунд,&nbsp;чтобы убедиться, что элемент не появился. Если мы используем нашу написанную функцию is_element_present, то тест с такой проверкой будет ждать полные и честные 10 секунд:</p>

<pre><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">should_not_be_success_message</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">)</span></span></span></span>:
    assert <span class="hljs-keyword"><span class="hljs-keyword">not</span></span> <span class="hljs-keyword"><span class="hljs-keyword">self</span></span>.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        <span class="hljs-string"><span class="hljs-string">"Success message is presented"</span></span></code></pre>

<p>Что очень много для зелёного теста. То есть implicit_wait уже в такой ситуации не подходит, придется использовать явное ожидание и аккуратно подбирать условия.&nbsp;Время ожидания тоже придется подбирать эмпирически, путем проб, ошибок, ложноположительных и ложноотрицательных результатов.&nbsp;</p>

<p><em>Во-вторых</em>, еще одна загвоздка с отрицательными проверками в том, что они могут давать ложноположительные срабатывания, если селектор устарел. Проверяем, что элемента с таким селектором нет,&nbsp;— проверка проходит, так как у элемента уже другой селектор. Элемент есть на экране&nbsp;— это&nbsp;баг, а тест зеленый. Это плохо!&nbsp;</p>

<p>Поэтому на каждый негативный тест обязательно должен приходиться положительный тест. В&nbsp;одном тесте проверяем, что элемента нет, в соседнем тесте, что элемент есть. Тогда мы сможем отслеживать актуальность селектора и не пропустим такой баг.&nbsp;</p>

<p>Дополнительная ссылка&nbsp;на пост Виталия Котова про распространенные грабли и отрицательные проверки, в том числе:</p>

<p>&nbsp;<a href="https://habr.com/ru/company/badoo/blog/419419/#no_element" rel="noopener noreferrer nofollow" target="_blank">UI-автотесты: как делать не стоит</a></p>

<h3>Как же тогда реализовывать такие проверки?&nbsp;</h3>

<p>Нужно ориентироваться на конкретную ситуацию, но общий совет — использовать явные ожидания и <a href="https://selenium-python.readthedocs.io/waits.html" rel="noopener noreferrer nofollow" target="_blank">Expected Conditions</a>, о которых мы говорили в предыдущих модулях.&nbsp;</p>

<p>Можно добавить в BasePage абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени:&nbsp;</p>

<pre><code class="hljs python"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">is_not_element_present</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, how, what, timeout=</span></span><span class="hljs-number"><span class="hljs-function"><span class="hljs-params"><span class="hljs-number">4</span></span></span></span><span class="hljs-function"><span class="hljs-params">)</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-keyword"><span class="hljs-keyword">try</span></span>:
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    <span class="hljs-keyword"><span class="hljs-keyword">except</span></span> TimeoutException:
        <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> <span class="hljs-keyword"><span class="hljs-keyword">True</span></span>

    <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> <span class="hljs-keyword"><span class="hljs-keyword">False</span></span></code></pre>

<p>Тогда его использование Page Object&nbsp;для&nbsp;страницы&nbsp;товара будет выглядеть так:&nbsp;</p>

<pre><code class="hljs ruby"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">should_not_be_success_message</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">)</span></span></span></span>:
    assert <span class="hljs-keyword"><span class="hljs-keyword">self</span></span>.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       <span class="hljs-string"><span class="hljs-string">"Success message is presented, but should not be"</span></span></code></pre>

<p>Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой&nbsp;результат&nbsp;мы ожидаем:&nbsp;</p>

<pre><code class="hljs python"><span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">is_disappeared</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self, how, what, timeout=</span></span><span class="hljs-number"><span class="hljs-function"><span class="hljs-params"><span class="hljs-number">4</span></span></span></span><span class="hljs-function"><span class="hljs-params">)</span></span></span><span class="hljs-function">:</span></span>
    <span class="hljs-keyword"><span class="hljs-keyword">try</span></span>:
        WebDriverWait(self.browser, timeout, <span class="hljs-number"><span class="hljs-number">1</span></span>, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
    <span class="hljs-keyword"><span class="hljs-keyword">except</span></span> TimeoutException:
        <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> <span class="hljs-keyword"><span class="hljs-keyword">False</span></span>

    <span class="hljs-keyword"><span class="hljs-keyword">return</span></span> <span class="hljs-keyword"><span class="hljs-keyword">True</span></span></code></pre>

<p>Метод-проверка в классе про страницу товара будет выглядеть аналогично <strong>should_not_be_success_message</strong>, напишите его самостоятельно.</p>

<p>&nbsp;</p>

<p>Обратите внимание на разницу между методами&nbsp;<strong>is_not_element_present</strong> и <strong>is_disappeared</strong>.&nbsp;</p>

<p><strong>is_not_element_present</strong>: упадет, как только&nbsp;увидит искомый элемент. Не появился: успех, тест зеленый.&nbsp;</p>

<p><strong>is_disappeared</strong>: будет ждать до тех пор, пока элемент не исчезнет.&nbsp;</p>

<p>&nbsp;</p>

<p>Резюмируя, можно сказать, что разрабатывать такие проверки нужно очень аккуратно, использовать явные ожидания для&nbsp;сокращения&nbsp;времени прогона&nbsp;теста&nbsp;и всегда добавлять позитивную проверку на элемент в другом тесте.&nbsp;Без явной необходимости таких проверок лучше избегать.&nbsp;</p></span>


<span><h2>Плюсы наследования: магия ООП</h2>

<p>Если вы использовали ранее парадигму ООП при написании кода, то уже представляете, как хорошая архитектура может облегчить жизнь. В этом плане код автотестов ничем не отличается от кода приложений — мы можем использовать всё те же приёмы для организации методов.</p>

<p>Здесь мы рассмотрим лишь один из примеров: использование механизма наследования.</p>

<p>Мы уже немного использовали механизм наследования, когда сделали базовый класс для всех наших проверок BasePage, а от него наследовали&nbsp;все остальные Page Object: LoginPage, MainPage. Сейчас у нас в классе BasePage в основном технические детали — реализация поиска элементов, метод для открытия страницы и прохождения капчи. Но никто не мешает нам добавить туда элементы и методы, которые являются общими для всех страниц.</p>

<p><img alt="" src="https://ucarecdn.com/2acd9ef7-922b-4c65-8e61-0f2eeacae6d0/"></p>

<h3>&nbsp;</h3>

<p><strong>ВАЖНО! </strong>Не нужно запихивать в базовый класс все, что плохо лежит и может когда-нибудь пригодиться. Добавлять нужно только то, что ОБЯЗАТЕЛЬНО будет на каждой странице-наследнике, иначе есть риск, что увеличение строк кода в файле&nbsp;будет неконтролируемым,&nbsp;и поддерживать его будет сложно.</p>

<p>Вообще говоря, мы можем строить какую угодно иерархию наших классов для взаимодействия с веб-приложением, если это поможет избежать дублирования кода. Например, есть набор страниц с общими методами, мы можем организовать их в виде наследования с дополнительным "слоем".</p>

<p>Например, когда мы тестируем страницу урока в Stepik (это&nbsp;та страница,&nbsp;на которой вы сейчас находитесь),&nbsp;мы используем LessonPage как базовый класс, где содержатся общие элементы и методы для всех типов шагов (шапка, комментарии, боковое расписание) и класс-наследник для каждого типа заданий, а их на&nbsp;Stepik более 20, каждый со своими уникальными методами и элементами.&nbsp;Такой подход&nbsp;позволяет избежать дублирования кода,&nbsp;и необходимости поддерживать файл на &gt;1000 строк кода.&nbsp;</p>

<p><a rel="noopener noreferrer nofollow"><img alt="" src="https://ucarecdn.com/89714d1e-9f92-46cb-af3f-0fab732f388b/"></a></p></span>

<span><h2><strong>Плюсы наследования: пример</strong></h2>

<p>В предыдущем уроке, мы написали тест "гость может&nbsp;перейти на страницу логина с главной страницы магазина". Но если вы внимательно посмотрите на остальные страницы, то заметите, что ссылка на страницу логина присутствует на каждой странице. Если мы хотим добавить тест "гость может перейти на страницу логина со страницы товара", то для избежания дублирования, логично перенести соответствующие методы в класс <strong>BasePage</strong>. Давайте так и поступим:&nbsp;</p>

<p>В файле <em>locators.py</em> создаем новый класс <strong>BasePageLocators</strong><em>&nbsp;</em>и переносим туда соответствующие элементы:</p>

<pre><code class="hljs stylus">class BasePageLocators():
    LOGIN_LINK = (By<span class="hljs-selector-class"><span class="hljs-selector-class">.CSS_SELECTOR</span></span>, <span class="hljs-string"><span class="hljs-string">"#login_link"</span></span>)
    LOGIN_LINK_INVALID = (By<span class="hljs-selector-class"><span class="hljs-selector-class">.CSS_SELECTOR</span></span>, <span class="hljs-string"><span class="hljs-string">"#login_link_inc"</span></span>)</code></pre>

<p>В файл <em>base_page.py</em> переносим соответствующие методы, заменяя класс с локаторами на BasePageLocators:&nbsp;&nbsp;</p>

<pre><code class="hljs python"><span class="hljs-keyword"><span class="hljs-keyword">from</span></span> .locators <span class="hljs-keyword"><span class="hljs-keyword">import</span></span> BasePageLocators


<span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">BasePage</span></span></span><span class="hljs-params"><span class="hljs-class"><span class="hljs-params">()</span></span></span><span class="hljs-class">:</span></span>
...
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">go_to_login_page</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">should_be_login_link</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(self)</span></span></span><span class="hljs-function">:</span></span>
        <span class="hljs-keyword"><span class="hljs-keyword">assert</span></span> self.is_element_present(*BasePageLocators.LOGIN_LINK), <span class="hljs-string"><span class="hljs-string">"Login link is not presented"</span></span>
<span class="hljs-meta"><span class="hljs-meta">... </span></span></code></pre>

<p><em>Примечание: методы лучше всего описывать в классе в алфавитном порядке, так проще ориентироваться и находить.</em></p>

<p>В классе&nbsp;<strong>MainPage</strong><em>&nbsp;</em>у нас не осталось никаких методов, поэтому добавим туда заглушку:&nbsp;</p>

<pre><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword"><span class="hljs-class"><span class="hljs-keyword">class</span></span></span><span class="hljs-class"> </span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">MainPage</span></span></span><span class="hljs-class">(</span><span class="hljs-title"><span class="hljs-class"><span class="hljs-title">BasePage</span></span></span><span class="hljs-class">):</span></span>
    <span class="hljs-function"><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-keyword">def</span></span></span><span class="hljs-function"> </span><span class="hljs-title"><span class="hljs-function"><span class="hljs-title">__init__</span></span></span><span class="hljs-params"><span class="hljs-function"><span class="hljs-params">(</span></span><span class="hljs-keyword"><span class="hljs-function"><span class="hljs-params"><span class="hljs-keyword">self</span></span></span></span><span class="hljs-function"><span class="hljs-params">, *args, **kwargs)</span></span></span></span>:
        <span class="hljs-keyword"><span class="hljs-keyword">super</span></span>(MainPage, <span class="hljs-keyword"><span class="hljs-keyword">self</span></span>).__init_<span class="hljs-number"><span class="hljs-number">_</span></span>(*args, **kwargs)</code></pre>

<p>Как вы уже знаете, метод<strong> __init__ </strong>вызывается при создании объекта. Конструктор выше с ключевым словом <strong>super&nbsp;</strong>на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор <strong>MainPage</strong>.&nbsp;</p>

<p>Теперь мы можем легко добавлять тесты вида "гость может перейти на страницу логина со страницы Х".&nbsp;</p>

<p>Добавляем в файл c тестами <em>test_product_page.py</em> новые тесты:&nbsp;</p>

<pre><code class="hljs routeros">def test_guest_should_see_login_link_on_product_page(browser):
    link = <span class="hljs-string"><span class="hljs-string">"http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"</span></span>
   <span class="hljs-built_in"><span class="hljs-built_in"> page </span></span>= ProductPage(browser, link)
    page.open()
    page.should_be_login_link()</code></pre>

<p>Добавьте самостоятельно второй тест&nbsp;</p>

<pre><strong>test_guest_can_go_to_login_page_from_product_page</strong>&nbsp;
</pre>

<p>Запустите тесты и убедитесь, что они проходят.&nbsp;</p>

<p>Зафиксируйте изменения коммитом.&nbsp;</p></span>






































