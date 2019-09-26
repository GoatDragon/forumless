        function regToggle() {
            log = document.getElementById("logdrop")
            reg = document.getElementById("regdrop")
            if (reg.className.match("drophide")) {
                reg.className = "dropshow";
                log.className = "drophide";
            }
            else {
                reg.className = "drophide";
            }
        }

        function logToggle() {
            log = document.getElementById("logdrop")
            reg = document.getElementById("regdrop")
            if (log.className.match("drophide")) {
                log.className = "dropshow";
                reg.className = "drophide";
            }
            else {
                log.className = "drophide";
            }
        }
        
        function postToggle() {
            post = document.getElementById("postdrop")
            if (post.className.match("drophide")) {
                post.className = "postshow";
            }
            else {
                post.className = "drophide";
            }
        }