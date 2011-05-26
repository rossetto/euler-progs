
        integer*8 sprimes
        integer k

        sprimes = 0
        do i=2,2000000
                nd = 0
                k = 2
                do while (k.le.int(i/k))
                        if (mod(i,k).eq.0) then
                                nd = 1
                                goto 10
                        endif
                        k = k + 1
                enddo
                if (nd.eq.0) then
                        sprimes=sprimes+i
                endif
  10    enddo
        print *, sprimes

        stop
        end
