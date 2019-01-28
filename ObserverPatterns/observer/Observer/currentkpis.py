from observer import AbcObserver

class CurrentKPIs(AbcObserver):
    open_tickets = -1
    close_ticktes = -1
    new_ticlets = -1

    def update(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def displat(self):
        print("Current open tickets: {}".format(self.open_tickets))
        print("New tickets in last hour: {}".format(self.new_ticlets))
        print("Tickets closed in last hour: {}".format(self.new_ticlets))
        print('*******\n')
        