from mamba import description, before, context, it, _it
from expects import expect, equal, raise_error, have_len
import xml.etree.ElementTree as ET
import subprocess

with description("Integration tests") as self:
    with it("should produce the expected graphml"):
        result = subprocess.check_output("bunnyplot http://localhost:15672 ./out.graphml -u guest -p guest", shell=True)
        
        ns = {'g': 'http://graphml.graphdrawing.org/xmlns'}
        root = ET.parse('./out.graphml').getroot()

        print(root)
        nodes = root.findall(".//g:node", ns)
        edges = root.findall(".//g:edge", ns)

        expect(nodes).to(have_len(13))
        expect(edges).to(have_len(11))