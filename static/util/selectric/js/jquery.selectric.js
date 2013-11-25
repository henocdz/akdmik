/*!
 *         ,/
 *       ,'/
 *     ,' /
 *   ,'  /_____,
 * .'____    ,'
 *      /  ,'
 *     / ,'
 *    /,'
 *   /'
 *
 * Selectric Ϟ v1.5.1 - http://lcdsantos.github.io/jQuery-Selectric/
 *
 * Copyright (c) 2013 Leonardo Santos; Dual licensed: MIT/GPL
 *
 */

;(function ($) {
	var pluginName = 'selectric',
		emptyFn = function() {},
		// Replace diacritics
		_replaceDiacritics = function(s) {
			/*
				/[\340-\346]/g, // a
				/[\350-\353]/g, // e
				/[\354-\357]/g, // i
				/[\362-\370]/g, // o
				/[\371-\374]/g, // u
				/[\361]/g, // n
				/[\347]/g, // c
				/[\377]/g // y
			*/
			var k, d = '40-46 50-53 54-57 62-70 71-74 61 47 77'.replace(/\d+/g, '\\3$&').split(' ');

			for (k in d)
				s = s.toLowerCase().replace(RegExp('[' + d[k] + ']', 'g'), 'aeiouncy'.charAt(k));

			return s;
		},
		init = function(element, options) {
			var options = $.extend({
					onOpen: emptyFn,
					onClose: emptyFn,
					maxHeight: 300,
					keySearchTimeout: 500,
					arrowButtonMarkup: '<b class="button">&#9662;</b>',
					disableOnMobile: true,
					border: 1
				}, options);

			if (options.disableOnMobile && /android|ip(hone|od|ad)/i.test(navigator.userAgent)) return;

			var $original = $(element),
				$wrapper = $('<div class="' + pluginName + '"><p class="label"/>' + options.arrowButtonMarkup + '</div>'),
				$items = $('<div class="' + pluginName + 'Items"><ul/></div>'),
				$outerWrapper = $original.data(pluginName, options).wrap('<div>').parent().append($wrapper).append($items),
				selectItems = [],
				isOpen = false,
				$label = $('.label', $wrapper),
				$ul = $('ul', $items),
				$li,
				bindSufix = '.sl',
				$doc = $(document),
				$win = $(window),
				keyBind = 'keydown' + bindSufix,
				clickBind = 'click' + bindSufix,
				searchStr = '',
				resetStr,
				classOpen = pluginName + 'Open',
				classDisabled = pluginName + 'Disabled',
				tempClass = pluginName + 'TempShow',
				selectStr = 'selected',
				selected,
				itemsHeight;

			function _populate() {
				var $options = $('option', $original.wrap('<div class="' + pluginName + 'HideSelect">')),
					_$li = '',
					visibleParent = $items.closest(':visible').children().not(':visible'),
					maxHeight = options.maxHeight,
					optionsLength;

				selected = $options.filter(':' + selectStr).index();

				if ( optionsLength = $options.length ) {
					// Build options markup
					$options.each(function(i, elm){
						var selectText = $(elm).text();

						selectItems[i] = {
							value: $(elm).val(),
							text: selectText,
							slug: _replaceDiacritics(selectText)
						};

						_$li += '<li class="' + (i == selected ? selectStr : '') + (i == optionsLength - 1 ? ' last' : '') + '">' + selectText + '</li>';
					});

					$ul.empty().append(_$li);
					$label.text(selectItems[selected].text);
				}

				$wrapper.add($original).off(bindSufix);
				$outerWrapper.prop('class', pluginName + 'Wrapper ' + $original.prop('class') + ' ' + classDisabled);

				if (!$original.prop('disabled')){
					// Not disabled, so... Removing disabled class and bind hover
					$outerWrapper.removeClass(classDisabled).hover(function(){
						$(this).toggleClass(pluginName + 'Hover');
					});

					// Click on label and :focus on original select will open the options box
					$wrapper.on(clickBind, function(e){
						isOpen ? _close(e) : _open(e);
					});

					$original.on(keyBind, function(e){
						e.preventDefault();

						var key = e.which;

						// Tab / Enter / ESC
						if (/^(9|13|27)$/.test(key)) {
							e.stopPropagation();
							_select(selected, true);
						}

						// Search in select options
						clearTimeout(resetStr);

						// If it's not a directional key
						if (key < 37 || key > 40) {
							var rSearch = RegExp('^' + (searchStr += String.fromCharCode(key)), 'i');

							$.each(selectItems, function(i, elm){
								if (rSearch.test([elm.slug, elm.text]))
									_select(i);
							});

							resetStr = setTimeout(function(){
								searchStr = '';
							}, options.keySearchTimeout);
						} else {
							searchStr = '';

							// Right / Down : Left / Up
							_select(/^(39|40)$/.test(key) ? (selected + 1) % optionsLength : (selected > 0 ? selected : optionsLength) - 1);
						}
					}).on('focusin' + bindSufix, function(e){
						isOpen || _open(e);
					});

					// Remove styles from items box
					// Fix incorrect height when refreshed is triggered with fewer options
					$li = $('li', $items.removeAttr('style')).click(function(){
						// The second parameter is to close the box after click
						_select($(this).index(), true);

						// Chrome doesn't close options box if select is wrapped with a label
						// We need to 'return false' to avoid that
						return false;
					});
				}

				// Calculate options box height
				// Set a temporary class on the hidden parent of the element
				visibleParent.addClass(tempClass);

				// Set the dimensions
				$items.width($wrapper.outerWidth() - (options.border * 2)).height() > maxHeight && $items.height(maxHeight);

				// Remove the temporary class
				visibleParent.removeClass(tempClass);
			}

			_populate();

			// Open the select options box
			function _open(e) {
				e.preventDefault();
				e.stopPropagation();

				// Find any other opened instances of select and close it
				$('.' + classOpen + ' select')[pluginName]('close');

				isOpen = true;
				itemsHeight = $items.show().height();

				_isInViewport();

				var scrollTop = $win.scrollTop();
				e.type == 'click' && $original.focus();
				$win.scrollTop(scrollTop);

				$doc.on(clickBind, _close);
				$outerWrapper.addClass(classOpen);
				_detectItemVisibility(selected);

				options.onOpen.call(this);
			}

			// Detect is the options box is inside the window
			function _isInViewport() {
				if (isOpen){
					$items.css('top', ($outerWrapper.offset().top + $outerWrapper.outerHeight() + itemsHeight > $win.scrollTop() + $win.height()) ? -itemsHeight : '');
					setTimeout(_isInViewport, 100);
				}
			}

			// Close the select options box
			function _close() {
				var selectedTxt = selectItems[selected].text;
				$items.hide();
				selectedTxt != $label.text() && $original.change();
				$label.text(selectedTxt);
				$outerWrapper.removeClass(classOpen);
				isOpen = false;
				$doc.off(bindSufix);
				options.onClose.call($original.blur());
			}

			// Select option
			function _select(index, close) {
				// If 'close' is false (default), the options box won't close after
				// each selected item, this is necessary for keyboard navigation
				$original.prop('value', selectItems[selected = index].value).find('option').eq(index).prop(selectStr, true);
				$li.removeClass(selectStr).eq(index).addClass(selectStr);
				_detectItemVisibility(index);
				close && _close();
			}

			// Detect if currently selected option is visible and scroll the options box to show it
			function _detectItemVisibility(index) {
				var liHeight = $li.eq(index).outerHeight(),
					liTop = $li[index].offsetTop,
					itemsScrollTop = $items.scrollTop(),
					itemsHeight = $items.height(),
					scrollT = liTop + liHeight * 2;

				$items.scrollTop(
					(scrollT > itemsScrollTop + itemsHeight) ? scrollT - itemsHeight :
						(liTop - liHeight < itemsScrollTop) ? liTop - liHeight :
							itemsScrollTop
				);
			}

			$original.on({
				refresh: _populate,
				destroy: function() {
					// Unbind and remove
					$items.remove();
					$wrapper.remove();
					$original.removeData(pluginName).off(bindSufix + ' refresh destroy open close').unwrap().unwrap();
				},
				open: _open,
				close: _close
			});
		};

	// A really lightweight plugin wrapper around the constructor,
	// preventing against multiple instantiations
	$.fn[pluginName] = function(args, options) {
		return this.each(function() {
			if (!$(this).data(pluginName)) {
				// new Selectric(this, args || options);
				init(this, args || options);
			} else if (''+args === args) {
				$(this).trigger(args);
			}
		});
	};
}(jQuery));