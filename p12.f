
        integer*8 t
        integer d

        j = 1
        t = 0
        d = 0
        do while (d.lt.500)
                d = 0
                t = 0
                do i=1,j
                        t = t + i
                enddo
                k = 2
                do while (k.lt.int(t/k))
                        if (mod(t,k).eq.0) then 
                                if (k*k.eq.t) then
                                        d = d + 1
                                else
                                        d = d + 2
                                endif
                        endif
                        k = k + 1
                enddo
                d = d + 1
                j = j + 1
        enddo

        print *, t, d

        stop
        end
