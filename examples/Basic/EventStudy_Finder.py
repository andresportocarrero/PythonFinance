from datetime import datetime
from finance.utils import DataAccess
from finance.events import SampleEvents
from finance.events import EventFinder

DataAccess.path = 'data'
da = DataAccess()

evtf = EventFinder()
evtf.symbols = ['AMD', 'CBG', 'AAPL']
evtf.start_date = datetime(2008, 1, 1)
evtf.end_date = datetime(2010, 12, 31)
evtf.event = SampleEvents.went_below(10)
evtf.search(useCache=False)

print(evtf.num_events)
# print(evtf.list)