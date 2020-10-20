# selenium_course__Page_Object

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
- **cd $HOME/selenium_course__Page_Objec;pytest -v --tb=line --language=en test_main_page.py**
- **conda deactivate; source $HOME/enviroments/selenium_env/bin/activate**



git clone https://github.com/mirpribili/simpler.git


# Page_Object

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













