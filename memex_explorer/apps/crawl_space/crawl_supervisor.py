"""Crawl Supervisor is a free-standing script that monitors and logs output
from crawl processes.

At the moment, this is a thin wrapper for the purpose of development. In
production systems, Memex Explorer should leverage a job queue
that manages crawl processes on distributed systems.


Example
-------

    $ python crawl_supervisor.py --project project_slug --crawl crawl_slug

"""

import argparse
import inspect

from apps.crawl_space.crawl_runners import AcheCrawlRunner, NutchCrawlRunner
from apps.crawl_space.utils import get_crawl


def parse_args():
    """Helper function to parse command line arguments.

    Arguments
    ---------

    -p, --project : str, required
        Project slug
    -c, --crawl : str, required
        Crawl slug

    Returns
    -------

    argparse.Namespace    
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", dest="project_slug", type=str,
                        required=True, help="Project slug")
    parser.add_argument("-c", "--crawl", dest="crawl_slug", type=str,
                        required=True, help="Crawl slug")
    return parser.parse_args()




class CrawlSupervisor(object):
    """Wraps crawl process execution.

    Parameters
    ----------

    project_slug : str, required
    crawl_slug : str, required

    Attributes
    ----------

    crawl_model : crawl_space.models.CrawlModel
    crawl : crawl_space.crawls.CrawlRunner subclass
        Currently supports AcheCrawlRunner and NutchCrawlRunner.
    """

    def __init__(self, *args, **kwargs):

        c = self.crawl_model = get_crawl(
            kwargs['project_slug'],
            kwargs['crawl_slug'])

        if c.crawler == 'ache':
            self.crawl = AcheCrawlRunner(c)

        elif c.crawler == 'nutch':
            self.crawl = NutchCrawlRunner(c)

    def start(self):
        """Start the crawl process.""" 
        self.crawl.run()


if __name__ == "__main__":

    import django
    django.setup()

    args = parse_args()
    crawl_supervisor = CrawlSupervisor(**vars(args))
    crawl_supervisor.start()
