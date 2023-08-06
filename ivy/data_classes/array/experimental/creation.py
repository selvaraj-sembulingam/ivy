# global
import abc
from typing import Optional, Union

# local
import ivy


class _ArrayWithCreationExperimental(abc.ABC):
    def eye_like(
        self: ivy.Array,
        /,
        *,
        k: int = 0,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        device: Optional[Union[ivy.Device, ivy.NativeDevice]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.eye_like. This method simply wraps the
        function, and so the docstring for ivy.eye_like also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            input array from which to derive the output array shape.
        k
            index of the diagonal. A positive value refers to an upper diagonal,
            a negative value to a lower diagonal, and 0 to the main diagonal.
            Default: ``0``.
        dtype
            output array data type. If ``dtype`` is ``None``, the output array data type
            must be inferred from ``self``. Default: ``None``.
        device
            device on which to place the created array. If ``device`` is ``None``, the
            output array device must be inferred from ``self``. Default: ``None``.
        out
            optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            an array having the same shape as ``self`` and filled with ``ones``
            in diagonal ``k`` and ``zeros`` elsewhere.

        Examples
        --------
        >>> x = ivy.array([[2, 3, 8],[1, 2, 1]])
        >>> y = x.eye_like()
        >>> print(y)
        ivy.array([[1., 0., 0.],
                    0., 1., 0.]])
        """
        return ivy.eye_like(self._data, k=k, dtype=dtype, device=device, out=out)

    def unsorted_segment_min(
        self: ivy.Array,
        segment_ids: ivy.Array,
        num_segments: Union[int, ivy.Array],
    ) -> ivy.Array:
        r"""
        ivy.Array instance method variant of ivy.unsorted_segment_min. This method
        simply wraps the function, and so the docstring for ivy.unsorted_segment_min
        also applies to this method with minimal changes.

        Note
        ----
        If the given segment ID `i` is negative, then the corresponding
        value is dropped, and will not be included in the result.

        Parameters
        ----------
        self
            The array from which to gather values.

        segment_ids
            Must be in the same size with the first dimension of `self`. Has to be
            of integer data type. The index-th element of `segment_ids` array is
            the segment identifier for the index-th element of `self`.

        num_segments
            An integer or array representing the total number of distinct segment IDs.

        Returns
        -------
        ret
            The output array, representing the result of a segmented min operation.
            For each segment, it computes the min value in `self` where `segment_ids`
            equals to segment ID.
        """
        return ivy.unsorted_segment_min(self._data, segment_ids, num_segments)

    def unsorted_segment_sum(
        self: ivy.Array,
        segment_ids: ivy.Array,
        num_segments: Union[int, ivy.Array],
    ) -> ivy.Array:
        r"""
        ivy.Array instance method variant of ivy.unsorted_segment_sum. This method
        simply wraps the function, and so the docstring for ivy.unsorted_segment_sum
        also applies to this method with minimal changes.

        Parameters
        ----------
        self
            The array from which to gather values.

        segment_ids
            Must be in the same size with the first dimension of `self`. Has to be
            of integer data type. The index-th element of `segment_ids` array is
            the segment identifier for the index-th element of `self`.

        num_segments
            An integer or array representing the total number of distinct segment IDs.

        Returns
        -------
        ret
            The output array, representing the result of a segmented sum operation.
            For each segment, it computes the sum of values in `self` where
            `segment_ids` equals to segment ID.
        """
        return ivy.unsorted_segment_sum(self._data, segment_ids, num_segments)
