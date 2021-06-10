JS_DROP_FILES = """
        var c = arguments,
        b = c[0],
        k = c[1];
        c = c[2];
        for (var d = b.ownerDocument || document, l = 0;;) {
            var e = b.getBoundingClientRect(),
            g = e.left + (k || e.width / 2),
            h = e.top + (c || e.height / 2),
            f = d.elementFromPoint(g, h);
            if (f && b.contains(f)) break;
            if (1 < ++l) throw b = Error('Element not interactable'),
            b.code = 15,
            b;
            b.scrollIntoView({
                behavior: 'instant',
                block: 'center',
                inline: 'center'
            })
        }
        var a = d.createElement('INPUT');
        a.setAttribute('type', 'file');
        a.setAttribute('multiple', '');
        a.setAttribute('style', 'position:fixed;z-index:2147483647;left:0;top:0;');
        a.onchange = function(b) {
            a.parentElement.removeChild(a);
            b.stopPropagation();
            var c = {
                constructor: DataTransfer,
                effectAllowed: 'all',
                dropEffect: 'none',
                types: ['Files'],
                files: a.files,
                setData: function() {},
                getData: function() {},
                clearData: function() {},
                setDragImage: function() {}
            };
            window.DataTransferItemList && (c.items = Object.setPrototypeOf(Array.prototype.map.call(a.files,
            function(a) {
                return {
                    constructor: DataTransferItem,
                    kind: 'file',
                    type: a.type,
                    getAsFile: function() {
                        return a
                    },
                    getAsString: function(b) {
                        var c = new FileReader;
                        c.onload = function(a) {
                            b(a.target.result)
                        };
                        c.readAsText(a)
                    }
                }
            }), {
                constructor: DataTransferItemList,
                add: function() {},
                clear: function() {},
                remove: function() {}
            }));
            ['dragenter', 'dragover', 'drop'].forEach(function(a) {
                var b = d.createEvent('DragEvent');
                b.initMouseEvent(a, !0, !0, d.defaultView, 0, 0, 0, g, h, !1, !1, !1, !1, 0, null);
                Object.setPrototypeOf(b, null);
                b.dataTransfer = c;
                Object.setPrototypeOf(b, DragEvent.prototype);
                f.dispatchEvent(b)
            })
        };
        d.documentElement.appendChild(a);
        a.getBoundingClientRect();
        return a;
        """
