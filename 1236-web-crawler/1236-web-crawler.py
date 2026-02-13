# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

# The function dfs is as follows:

# dfs(url)

# Add url to the hash set visited.
# Iterate over the list htmlParser.getUrls(url) of all URLs from a webpage of url. Let call the current element of this list nextUrl.
# If nextUrl has the same hostname as the start URL and the set visited does not contain nextUrl, call dfs(nextUrl) recursively.

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            # split url by slashes
            # for instance, "http://example.org/foo/bar" will be split into
            # "http:", "", "example.org", "foo", "bar"
            # the hostname is the 2-nd (0-indexed) element
            return url.split('/')[2]

        start_hostname = get_hostname(startUrl)
        visited = set()

        def dfs(url, htmlParser):
            visited.add(url)
            for next_url in htmlParser.getUrls(url):
                if get_hostname(next_url) == start_hostname and next_url not in visited:
                    dfs(next_url, htmlParser)

        dfs(startUrl, htmlParser)
        return visited

# Let m be the number of edges in the graph, and l be the maximum length of a URL (urls[i].length).

# Time complexity: O(m⋅l).

    
        