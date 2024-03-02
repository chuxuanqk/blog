---
title:  Linux 串口编程
date: 2020-03-11 11:41:10
tags: 
categories: 

---

Linux 串口编程

<!-- more -->



<h1 align = "center">Linux 串口编程</h1>



**1.串口接收超时设置**

```c
// 接收单字节
int _uart_recv_byte(miio_uart_t *uart, uint8_t* c, uint32_t timeout_ms)
{
	/* the following is an example for linux platform */
	/* user should adjust below for each mcu platform */
	/* adjust start */
	struct termios opt;	/* set uart timeout */
	tcgetattr(uart->fd, &opt);
	opt.c_cc[VTIME] = timeout_ms / 100; 
	tcsetattr(uart->fd, TCSADRAIN, &opt);
	/* adjust end */

	arch_os_mutex_get(&(uart->read_mutex));
	/* adjust start */
	int n_read = read(uart->fd, c, 1);
	/* adjust end */
	arch_os_mutex_put(&(uart->read_mutex));

	return n_read;
}

// 接收多个字节
int _Xmodem_recv_str(miio_uart_t *uart, uint8_t* buf, uint32_t timeout_ms)
{
        /* the following is an example for linux platform */
        /* user should adjust below for each mcu platform */
        /* adjust start */
        struct termios opt;     /* set uart timeout */
        tcgetattr(uart->fd, &opt);
        opt.c_cc[VTIME] = timeout_ms / 100;// / 100;
        tcsetattr(uart->fd, TCSADRAIN, &opt);
        /* adjust end */
        arch_os_mutex_get(&(uart->read_mutex));
        /* adjust start */
        int n_read = read(uart->fd, buf, USER_UART_RXBUF_SIZE);
        buf[n_read] = '\0';
        /* adjust end */
        arch_os_mutex_put(&(uart->read_mutex));

        return n_read;
}
```

