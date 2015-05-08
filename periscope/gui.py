#!/usr/bin/env python
import ttk
import Tkinter

import tests

class Wizard(object, ttk.Notebook):
    def __init__(self, master=None, **kw):
        npages = kw.pop('npages', 3)
        kw['style'] = 'Wizard.TNotebook'
        ttk.Style(master).layout('Wizard.TNotebook.Tab', '')
        ttk.Notebook.__init__(self, master, **kw)

        self._children = {}

        for page in range(npages):
            self.add_empty_page()

        self.current = 0
        self._wizard_buttons()

    def _wizard_buttons(self):
        """Place wizard buttons in the pages."""
        for indx, child in self._children.iteritems():
            btnframe = ttk.Frame(child)
            btnframe.pack(side='bottom', fill='x', padx=6, pady=12)

            nextbtn = ttk.Button(btnframe, text="Next", command=self.next_page)
            nextbtn.pack(side='right', anchor='e', padx=6)
            if indx != 0:
                prevbtn = ttk.Button(btnframe, text="Previous",
                    command=self.prev_page)
                prevbtn.pack(side='right', anchor='e', padx=6)

                if indx == len(self._children) - 1:
                    nextbtn.configure(text="Finish", command=self.close)

    def next_page(self):
        self.current += 1

    def prev_page(self):
        self.current -= 1

    def close(self):
        self.master.destroy()

    def add_empty_page(self):
        child = ttk.Frame(self)
        self._children[len(self._children)] = child
        self.add(child)

    def add_page_body(self, body):
        body.pack(side='top', fill='both', padx=6, pady=12)

    def page_container(self, page_num):
        if page_num in self._children:
            return self._children[page_num]
        else:
            raise KeyError("Invalid page: %s" % page_num)

    def _get_current(self):
        return self._current

    def _set_current(self, curr):
        if curr not in self._children:
            raise KeyError("Invalid page: %s" % curr)

        self._current = curr
        self.select(self._children[self._current])

    current = property(_get_current, _set_current)

class gui:
    def __init__(self, periscope):
        self.periscope = periscope
        root = Tkinter.Tk()
        root.title("Periscope")
        wizard = Wizard(npages=4)
        wizard.master.minsize(600, 400)
        self.welcome_page(wizard)
        self.acknowledge_page(wizard)
        self.level_page(wizard)
        self.test_page(wizard)
        wizard.pack(fill='both', expand=True)
        root.mainloop()

    def welcome_page(self, root):
        page = root.page_container(0)
        title = ttk.Label(page, text='Periscope', font='bold 28', anchor='s').pack(ipady=10)
        subtitle = ttk.Label(page, text='Tor Censorship Detector', font='24',
                foreground='grey').pack()
        logo = Tkinter.PhotoImage(file='resources/logo.gif')
        image = Tkinter.Label(page, image=logo, anchor='s')
        image.pack(padx=20, ipady=20)
        image.image = logo

    def acknowledge_page(self, root):
        acknowledge_text = \
                'Periscope is an automated tool for studying censorship ' \
                'of the Tor network. The Tor Censorship analyzer will conduct ' \
                'a number of tests to figure out if (and how) tor is being ' \
                'blocked.\n' \
                '\n'\
                'After the tests are run, Periscope may offer you advice on ' \
                'bypassing the censorship. \n'\
                '\n'\
                'Running Periscope may be dangerous in your country. Please '\
                'proceed with caution.'

        warning_text = \
                'If you do not wish to run Periscope, simply close this window.'

        placate_text = 'No tests will be run.'

        page = root.page_container(1)
        title = ttk.Label(page, text='Periscope', font='bold 18', anchor='w') \
                .pack(fill='both', padx=10, pady=5)
        information = ttk.Label(page, text=acknowledge_text, anchor='w',
                wraplength='600', font='18') \
                .pack(fill='both', padx=10, pady=15)
        warning = ttk.Label(page, text=warning_text, font='bold', anchor='sw',
                wraplength='600') \
                .pack(fill='both', padx=10)
        placate = ttk.Label(page, text=placate_text, font='18', anchor='w') \
                .pack(fill='both', padx=10)

    def level_page(self, root):

        def text_generator(risk):
            text = ''
            for test in self.periscope.TestManager.netTestsByRisk(risk):
                text = text + test.name + ": \n" + test.description + ".\n\n"
            self.riskText.set(text)

        page = root.page_container(2)
        title = ttk.Label(page, text='Intrusiveness', font='bold 18', anchor='w') \
                .pack(fill='both', padx=10, pady=5)
        slider_title = ttk.Label(page, text='Risk Level   At this risk '\
                'level, the following tests will be run:', font='16', anchor='w') \
                .pack(fill='x', padx=20)
        risk_slider = Tkinter.Scale(page, from_=5, to=1, orient='vertical',
                tickinterval=1, showvalue=False, command=text_generator) \
                .pack(fill='y', padx=30, pady=10, side='left')
        self.riskText = Tkinter.StringVar()
        risk_text = ttk.Label(page, textvariable=self.riskText,# font='14',
                anchor='sw', wraplength='600')\
                .pack(fill='both', padx=20, pady=20)

    def test_page(self, root):
        page = root.page_container(3)
        title = ttk.Label(page, text='Running Tests', font='bold 18', anchor='w') \
                .pack(fill='both', padx=10, pady=5)

        c_web = Tkinter.Checkbutton(page, state='disabled', text='Testing Official Website', anchor='w')
        c_web.select()
        c_web.pack(fill='x')

        dir_auths = Tkinter.Checkbutton(page, state='disabled', text='Probing Directory Authorities', anchor='w')
        dir_auths.pack(fill='x')

        relays = Tkinter.Checkbutton(page, text='Access to Relays')

        four = Tkinter.Checkbutton(page, text='Access to Bridges')

