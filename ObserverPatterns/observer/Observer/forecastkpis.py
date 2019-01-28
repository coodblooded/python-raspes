from observer import AbcObserver


class CurrentKPIs(AbcObserver):
    open_tickets = -1
    close_ticktes = -1
    new_ticlets = -1

    def update(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def displat(self):
        print("Forecast open tickets: {}".format(self.open_tickets))
        print("New tickets expected in next hour: {}".format(self.new_ticlets))
        print("Tickets expected to be  closed in next hour: {}".format(self.new_ticlets))
        print('*******\n')
